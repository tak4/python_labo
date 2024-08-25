import abc

class BaseDeserializer(metaclass=abc.ABCMeta):

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    @abc.abstractmethod
    def decode(self, input_file=None, output_file=None):
        pass
