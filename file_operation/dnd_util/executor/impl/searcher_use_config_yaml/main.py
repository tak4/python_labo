import sys
from gui_dnd.dnd_grep import QApplication, MainWindow
from executor.impl.searcher_use_config_yaml.searcher import FileKeywordSearcher

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(FileKeywordSearcher())
    window.show()
    sys.exit(app.exec())
