import abc

class BaseExecutor(abc.ABC):
    """ファイル処理のベースクラス
    """
    window_title = "Window"
    show_cancel_button = False

    @abc.abstractmethod
    def execute(self, paths: list, cancel_event=None, progress_callback=None):
        pass
