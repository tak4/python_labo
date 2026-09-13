import sys
from gui_dnd.dnd_grep import QApplication, MainWindow
from executor.impl.simple_searcher.searcher import SimpleSearcher

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(SimpleSearcher())
    window.show()
    sys.exit(app.exec())
