import sys
from gui_dnd.dnd_grep import QApplication, MainWindow
from searcher.impl.use_config_yaml.use_config_yaml_searcher import FileKeywordSearcher

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(FileKeywordSearcher())
    window.show()
    sys.exit(app.exec())
