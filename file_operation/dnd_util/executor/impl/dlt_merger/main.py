import sys
from gui_dnd.dnd_grep import QApplication, MainWindow
from executor.impl.dlt_merger.merger import DltMerger

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(DltMerger())
    window.show()
    sys.exit(app.exec())
