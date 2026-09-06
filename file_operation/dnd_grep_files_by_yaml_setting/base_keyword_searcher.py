import abc

class BaseSearcher(abc.ABC):
    """検索処理のベースクラス
    """
    @abc.abstractmethod
    def execute(self, cancel_event=None, progress_callback=None):
        pass
