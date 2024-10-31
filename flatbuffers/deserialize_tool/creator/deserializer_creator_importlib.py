import importlib
import deserializer.animal.animal_deserializer

class DesealizeCreator(object):

    @staticmethod
    def create(kind):

        deserializer = None

        class_name = kind.capitalize() + 'Deserializer'
        module_name = f'deserializer.{kind}.{kind}_deserializer'

        module = importlib.import_module(module_name)
        deserializer = getattr(module, class_name)
        print(f'create {type(deserializer)}')

        return deserializer()
