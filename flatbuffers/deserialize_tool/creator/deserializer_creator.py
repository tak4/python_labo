from deserializer.human.human_deserializer import HumanDeserializer
from deserializer.animal.animal_deserializer import AnimalDeserializer

class DesealizeCreator(object):

    @staticmethod
    def create(kind):

        deserializer = None
        if kind == 'human':
            deserializer = HumanDeserializer()
        elif kind == 'animal':
            deserializer = AnimalDeserializer()

        return deserializer
