"""ドラッグアンドドロップ指定したフォルダ内を検索する"""
import re
import sys
import yaml
import threading
from pathlib import Path
from pathlib import PurePosixPath
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtCore import QObject, pyqtSignal, QThread


class FileKeywordSearcher():
    """検索条件文字列(config.yaml)を元に指定フォルダ内を検索する
    """

    def __init__(self, paths: list):
        # 検索対象のパス 後のパス比較のため、パスを正規化(resolve)しておく
        self.paths = [Path(p) for p in paths]

        # 設定ファイル読み込み
        config_path = Path(__file__).parent / 'config' / 'config.yaml'
        with open(config_path, 'r', encoding='utf-8') as yaml_file:
            self.data = yaml.safe_load(yaml_file)


    def execute(self, cancel_event=None, progress_callback=None):
        """ 検索を行う
        """
        # Drag and Drop で取得したディレクトリを順に処理する
        for p in self.paths:
            if cancel_event is not None and cancel_event.is_set():
                break
            self._grep_path(p, cancel_event, progress_callback)


    def _natural_path_key(self, path):
        """ 検索結果ソート用の為のキー関数
        """
        key = []
        # as_posix()でパス区切り文字を/に統一する
        # OS異存の実ファイルパスではなく、文字列としてのパス表現で扱いたい為、
        # PurePosixPath を使用する
        for part in PurePosixPath(path.as_posix()).parts:
            m = re.search(r'(?i)(N)(\d+)', part)
            if m:
                prefix, number = m.groups()
                key.append((prefix or "", int(number), part.lower()))
            else:
                key.append(("", 0, part.lower()))
        return tuple(key)


    def _grep_path(self, target_path: Path, cancel_event=None, progress_callback=None):
        """ 指定パス内の検索を行う
        """

        # grep結果出力先ディレクトリを作成する
        output_folder = target_path.joinpath("output")
        output_folder.mkdir(exist_ok=True)

        # 検索条件(condition)ごとの処理
        for condition in self.data["search_conditions"]:
            if cancel_event is not None and cancel_event.is_set():
                break

            # 検索対象ファイル名を取得する
            files = self._get_rglob_file_list(target_path, condition["target_file"])

            # grep結果出力先ファイル名を取得
            output_file = output_folder / condition["output_file"]

            # grep実行
            self._do_regex_search(target_path, files, output_file, condition["keywords"], cancel_event, progress_callback)


    def _get_rglob_file_list(self, path: Path, target_files: list[str]) -> list[Path]:
        """ 検索対象ファイルをパス名＋ファイル名で取得する
        """

        # rglobでフルパス取得する 相対パスを得る処理の為、Pathオブジェクトで保持しておく
        target_file_list = []
        for target_file in target_files:
            target_file_list.extend([Path(p) for p in path.rglob(target_file)])

        return target_file_list


    def _do_regex_search(self, target_path: Path, target_files_with_path: list[Path], output_file: str, keywords: dict, cancel_event=None, progress_callback=None):
        """ リテラル／正規表現による検索を行う
        """

        # 検索条件の作成
        # リテラル (メタ文字をエスケープする)
        parts = [re.escape(k) for k in keywords.get('literal',[])]
        # 正規表現
        parts = parts + [k for k in keywords.get('regex',[])]

        pattern = "|".join(parts)
        pattern = r"(" + pattern + r")"
        flags = re.MULTILINE
        regex = re.compile(pattern, flags)

        # 相対パスにする為に、検索対象のパスを用意しておく
        base = Path(target_path).resolve()

        # 検索の実行
        # 結果をoutput_fileに出力する
        records = []
        total_files = len(target_files_with_path)
        try:
            with open(output_file, mode='w', encoding="utf-8", errors="ignore") as o_fp:    # 結果出力ファイル
                for index, target_file in enumerate(target_files_with_path, start=1):
                    if cancel_event is not None and cancel_event.is_set():
                        break

                    if progress_callback is not None:
                        progress_callback(f"検索中: {target_file.name}", index, total_files)

                    with open(target_file, mode='r', encoding="utf-8", errors="ignore") as i_fp:    # 検索対象ファイル
                        for i, line in enumerate(i_fp, start=1):
                            if regex.search(line):
                                # 検索結果のファイル名は相対パスにする
                                relative_path = target_file.relative_to(base)
                                # 検索結果をソートする為に一旦結果をリストで保持
                                records.append((relative_path, i, line.rstrip()))
                                
                for relative_path, i, line in sorted(records, key=lambda x: self._natural_path_key(x[0])):
                    o_fp.write(f"{relative_path}:{i}:{line}\n")

        except OSError as e:
            print(f"{e}")


class SearchWorker(QObject):
    progress = pyqtSignal(str, int, int)
    finished = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, paths, config_data):
        super().__init__()
        self.paths = paths
        self.config_data = config_data
        self.cancel_event = threading.Event()

    def cancel(self):
        self.cancel_event.set()

    def run(self):
        try:
            for p in self.paths:
                if self.cancel_event.is_set():
                    break

                self.progress.emit(f"検索中: {p}", 0, 1)
                searcher = FileKeywordSearcher([str(p)])
                searcher.data = self.config_data
                searcher.execute(cancel_event=self.cancel_event, progress_callback=lambda message, current, total: self.progress.emit(message, current, total))
            self.finished.emit()
        except Exception as e:
            self.error.emit(str(e))


class DropWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = QLabel("Please drop your folder here.")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            "QLabel { border: 2px dashed #888; font-size: 16px; padding: 20px; }"
        )
        self.setAcceptDrops(True)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 1)
        self.progress_bar.setValue(0)
        self.progress_bar.hide()

        self.cancel_btn = QPushButton("キャンセル")
        self.cancel_btn.hide()

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.cancel_btn)

    def update_status(self, message, current=0, total=0):
        self.label.setText(message)
        if total > 0:
            self.progress_bar.setRange(0, total)
            self.progress_bar.setValue(current)
            self.progress_bar.show()
        else:
            self.progress_bar.hide()

    def on_error(self, message):
        self.label.setText(f"Error: {message}")
        self.progress_bar.hide()

    def on_finished(self):
        if self.worker.cancel_event.is_set():
            self.label.setText("Cancelled")
        else:
            self.label.setText("Complete!")
        self.cancel_btn.hide()
        self.progress_bar.hide()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        mime = event.mimeData()
        if mime.hasUrls():
            paths = [url.toLocalFile() for url in mime.urls()]

            self.label.setText("検索中...")
            self.cancel_btn.show()

            self.thread = QThread()
            self.worker = SearchWorker(paths, FileKeywordSearcher(paths).data)

            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.progress.connect(self.update_status)
            self.worker.finished.connect(self.on_finished) 
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.error.connect(self.on_error)

            self.cancel_btn.clicked.connect(self.worker.cancel)

            self.thread.start()

        elif mime.hasText():
            self.setText("dropped text:\n" + mime.text())
        else:
            self.setText("This data is not supported.")
        event.acceptProposedAction()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("dnd grep files")
        self.resize(400, 250)

        layout = QVBoxLayout()
        layout.addWidget(DropWidget())

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
