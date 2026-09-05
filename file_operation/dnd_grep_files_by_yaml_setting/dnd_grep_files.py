"""ドラッグアンドドロップ指定したフォルダ内を検索する"""
import sys
import threading

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtCore import QObject, pyqtSignal, QThread

from keyword_searcher import KeywordSearcher

class SearchWorker(QObject):
    progress = pyqtSignal(str, int, int)
    finished = pyqtSignal()
    stopped = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, paths):
        super().__init__()
        self.paths = paths
        self.cancel_event = threading.Event()

    def cancel(self):
        self.cancel_event.set()

    def run(self):
        try:
            for p in self.paths:
                if self.cancel_event.is_set():
                    break

                self.progress.emit(f"検索中: {p}", 0, 1)
                searcher = KeywordSearcher([str(p)])
                searcher.execute(cancel_event=self.cancel_event, 
                                 progress_callback=lambda message, 
                                 current, 
                                 total: self.progress.emit(message, current, total))
            self.finished.emit()

        except Exception as e:
            self.error.emit(str(e))

        finally:
            self.stopped.emit()

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
        self.cancel_btn.hide()

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
            self.worker = SearchWorker(paths)

            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.progress.connect(self.update_status)
            self.worker.finished.connect(self.on_finished) 
            self.worker.stopped.connect(self.thread.quit)
            self.worker.stopped.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.error.connect(self.on_error)

            self.cancel_btn.clicked.connect(self.worker.cancel)

            self.thread.start()

        elif mime.hasText():
            self.label.setText("dropped text:\n" + mime.text())
        else:
            self.label.setText("This data is not supported.")
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
