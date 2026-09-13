"""ドラッグアンドドロップ指定したフォルダ内を検索する"""
import threading
import traceback

from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QProgressBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtCore import QObject, pyqtSignal, QThread

from searcher.base.base_searcher import BaseSearcher

class SearchWorker(QObject):
    """検索スレッドを構成するクラス
    """
    progress = pyqtSignal(str, int, int)
    finished = pyqtSignal(bool)
    stopped = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, searcher: BaseSearcher, paths: list[str]):
        super().__init__()

        self.searcher = searcher
        self.paths = paths
        self.cancel_event = threading.Event()

    def cancel(self):
        """キャンセルイベントをセット
        """
        self.cancel_event.set()

    def run(self):
        """検索スレッドによる検索処理
        """
        try:
            for p in self.paths:
                if self.cancel_event.is_set():
                    break

                self.progress.emit(f"検索中: {p}", 0, 1)
                self.searcher.execute([str(p)],
                                 cancel_event=self.cancel_event, 
                                 progress_callback=lambda message, 
                                 current, 
                                 total: self.progress.emit(message, current, total))

        except Exception as error:
            print(traceback.format_exc())
            self.error.emit(str(error))

        else:
            self.finished.emit(self.cancel_event.is_set())

        finally:
            self.stopped.emit()


class DropWidget(QWidget):
    def __init__(self, searcher: BaseSearcher, parent=None):
        super().__init__(parent)

        self.searcher = searcher
        self.thread = None
        self.worker = None

        self.label = QLabel("Please drop file here.")
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
        self.cancel_btn.clicked.connect(self.cancel_search)

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

    def on_finished(self, cancelled):
        """検索処理が正常終了したことを画面へ通知
        """
        self.label.setText("Cancelled" if cancelled else "Complete!")
        self.cancel_btn.hide()
        self.progress_bar.hide()

    def on_thread_finished(self):
        """QThread自体が終了した後の後始末
        """
        self.thread = None
        self.worker = None

    def dragEnterEvent(self, event: QDragEnterEvent):
        # 検索中は受付拒否
        if self.is_searching():
            event.ignore()
            return

        if event.mimeData().hasUrls() or event.mimeData().hasText():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        # 検索中は受付拒否
        if self.is_searching():
            event.ignore()
            return

        mime = event.mimeData()
        if mime.hasUrls():
            paths = [url.toLocalFile() for url in mime.urls()]

            self.label.setText("検索中...")
            self.cancel_btn.show()

            self.thread = QThread()
            self.worker = SearchWorker(self.searcher, paths)
            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.run)
            self.worker.progress.connect(self.update_status)
            self.worker.finished.connect(self.on_finished) 
            self.thread.finished.connect(self.on_thread_finished)
            self.thread.finished.connect(self.thread.deleteLater)
            self.worker.stopped.connect(self.thread.quit)
            self.worker.stopped.connect(self.worker.deleteLater)

            self.worker.error.connect(self.on_error)

            self.thread.start()

        elif mime.hasText():
            self.label.setText("dropped text:\n" + mime.text())
        else:
            self.label.setText("This data is not supported.")
        event.acceptProposedAction()

    def is_searching(self):
        """検索中を判定する
        """
        return self.thread is not None and self.thread.isRunning()

    def cancel_search(self):
        """キャンセル処理"""
        if self.worker is not None:
            self.worker.cancel()


class MainWindow(QMainWindow):
    def __init__(self, searcher: BaseSearcher):
        super().__init__()
        self.setWindowTitle("dnd grep files")
        self.resize(400, 250)

        layout = QVBoxLayout()
        layout.addWidget(DropWidget(searcher))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

