import abc

class DeserilizerCreator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create(self, type):
        pass
