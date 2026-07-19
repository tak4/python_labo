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

        target_files = {}
        p = Path(target_path)
        target_files = [str(p) for p in p.rglob('*.log')]

        # ダブルクォーテーションで囲まれた文字列を抜き出す
        pattern = r'.*"([^\"]+)".*'
        regex = re.compile(pattern)

        for target_file in target_files:
            with open(target_file, mode='r', encoding="utf-8", errors="ignore") as target_fp:
                for i, line in enumerate(target_fp, start=1):
                    # findall()を使用する
                    matches = regex.findall(line)
                    if matches:
                        for m in matches:
                            print(i, m)
                    # sub()を使用する
                    m = regex.search(line)
                    if m:
                        result = regex.sub(r'\g<1>', line)
                        print(i, result)


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
