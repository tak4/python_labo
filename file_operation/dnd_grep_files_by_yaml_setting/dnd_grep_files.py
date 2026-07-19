"""ドラッグアンドドロップ指定したフォルダ内を検索する"""
import os
import re
import sys
from typing import List
import yaml
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDragEnterEvent, QDropEvent


class FileKeywordSearcher():
    """
    """

    def __init__(self, paths: list):
        # 検索対象のパス
        self.paths = paths

        # 設定ファイル読み込み
        with open('./config/config.yaml', 'r') as yaml_file:
            self.data = yaml.safe_load(yaml_file)


    def search(self):
        """ 
        """
        # Drag and Drop で取得したディレクトリを順に処理する
        for p in self.paths:
            self._grep_path(p)


    def _grep_path(self, target_path: str):
        """ 
        """

        # grep結果出力先ディレクトリを作成する
        output_folder = os.path.join(target_path, 'output')
        os.makedirs(output_folder, exist_ok=True)

        # 検索条件を取得
        for condition in self.data['search_conditions']:
            # conditionごとの処理
            files = self._get_rglob_file_list(condition['target_file'])

            for f in files:
                print(f)

            # grep結果出力先ファイル
            output_file = os.path.join(output_folder, condition['output_file'])

            # grep
            self._do_reqex_search(files, output_file, condition['keywords'])


    def _get_rglob_file_list(self, target_files: List[str]) -> list:
        """
        """

        target_file_list = []
        for p in self.paths:
            p = Path(p)
            for target_file in target_files:
                target_file_list.extend([str(p) for p in p.rglob(target_file)])
        return target_file_list


    def _do_reqex_search(self, target_files: List[str], output_file: str, keywords: dict):
        """
        """

        # 検索条件の作成
        # リテラル (メタ文字をエスケープする)
        parts = [re.escape(k) for k in keywords['literal']]
        # 正規表現
        parts = parts + [k for k in keywords['regex']]

        pattern = "|".join(parts)
        pattern = r"(" + pattern + r")"
        flags = re.MULTILINE
        regex = re.compile(pattern, flags)

        try:
            with open(output_file, mode='w', encoding="utf-8", errors="ignore") as o_fp:
                for target_file in target_files:
                    with open(target_file, mode='r', encoding="utf-8", errors="ignore") as i_fp:
                        for i, line in enumerate(i_fp, start=1):
                            if regex.search(line):
                                wline = f"{target_file}:{i}:{line.rstrip()}"
                                o_fp.write("{}\n".format(wline))
        except (OSError,) as e:
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
            gp = FileKeywordSearcher(paths)
            gp.search()
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
