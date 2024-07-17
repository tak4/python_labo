import abc

class Deserializer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def decode(self):
        pass
