"""ドラッグアンドドロップ指定したフォルダ内を検索する"""
import re
import sys
import yaml
from pathlib import Path
from pathlib import PurePosixPath
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDragEnterEvent, QDropEvent


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


    def execute(self):
        """ 検索を行う
        """
        # Drag and Drop で取得したディレクトリを順に処理する
        for p in self.paths:
            self._grep_path(p)


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


    def _grep_path(self, target_path: Path):
        """ 指定パス内の検索を行う
        """

        # grep結果出力先ディレクトリを作成する
        output_folder = target_path.joinpath('output')
        output_folder.mkdir(exist_ok=True)   # parents=True も必要なら追加

        # 検索条件(condition)ごとの処理
        for condition in self.data['search_conditions']:
            # 検索対象ファイル名を取得する
            files = self._get_rglob_file_list(target_path, condition['target_file'])

            # grep結果出力先ファイル名を取得
            output_file = output_folder / condition['output_file']

            # grep実行
            self._do_regex_search(target_path, files, output_file, condition['keywords'])


    def _get_rglob_file_list(self, path: Path, target_files: list[str]) -> list[Path]:
        """ 検索対象ファイルをパス名＋ファイル名で取得する
        """

        # rglobでフルパス取得する 相対パスを得る処理の為、Pathオブジェクトで保持しておく
        target_file_list = []
        for target_file in target_files:
            target_file_list.extend([Path(p) for p in path.rglob(target_file)])

        return target_file_list


    def _do_regex_search(self, target_path: Path, target_files_with_path: list[Path], output_file: str, keywords: dict):
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
        try:
            with open(output_file, mode='w', encoding="utf-8", errors="ignore") as o_fp:    # 結果出力ファイル
                for target_file in target_files_with_path:
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


class DropLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Please drop your folder here.")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(
            "QLabel { border: 2px dashed #888; font-size: 16px; padding: 20px; }"
        )
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        mime = event.mimeData()
        if mime.hasUrls():
            paths = [url.toLocalFile() for url in mime.urls()]
            self.setText("dropped file:\n" + "\n".join(paths))
            try:
                gp = FileKeywordSearcher(paths)
                gp.execute()
                self.setText("Complete!")
            except Exception as e:
                self.setText(f"Error: {e}")
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
        layout.addWidget(DropLabel())

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
