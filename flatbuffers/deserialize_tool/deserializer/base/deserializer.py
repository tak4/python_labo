import abc

class BaseDeserializer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def decode(self, input_file=None, output_file=None):
        pass

    @abc.abstractmethod
    def decode_and_process(self, input_file=None) -> list[str]:
        pass
