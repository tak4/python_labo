import glob
import os
import sys
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QMimeData
from PyQt6.QtGui import QDragEnterEvent, QDropEvent


class GrepPaths():
    def __init__(self, paths: list):
        self.paths = paths

    def grep_target(self):
        self.paths
        for p in self.paths:
            self.grep_path(p)

    def grep_path(self, p: str):
        output_folder = os.path.join(p, 'output')
        os.makedirs(output_folder, exist_ok=True)

        files = self.get_target_file_list()
        for f in files:
            print(f)

    def get_target_file_list(self) -> list:
        for p in self.paths:
            p = Path(p)
            files = [str(p) for p in p.rglob('*.log')]
        return files

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
            gp = GrepPaths(paths)
            gp.grep_target()
        elif mime.hasText():
            self.setText("dropped text:\n" + mime.text())
        else:
            self.setText("This data is not supported.")
        event.acceptProposedAction()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Drag & Drop")
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