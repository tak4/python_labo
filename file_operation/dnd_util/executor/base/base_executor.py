import abc

class BaseExecutor(abc.ABC):
    """検索処理のベースクラス
    """
    @abc.abstractmethod
    def execute(self, paths: list, cancel_event=None, progress_callback=None):
        pass
