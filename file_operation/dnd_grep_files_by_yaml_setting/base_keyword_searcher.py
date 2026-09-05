import abc

class BaseSearcher(abc.ABC):
    @abc.abstractmethod
    def execute(self, cancel_event=None, progress_callback=None):
        pass
