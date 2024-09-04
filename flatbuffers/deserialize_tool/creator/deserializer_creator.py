from deserializer.human.human_deserializer import HumanDeserializer
from deserializer.animal.animal_deserializer import AnimalDeserializer

class DesealizeCreator(object):

    @classmethod
    def create(cls, kind):

        deserializer = None
        if kind == 'human':
            deserializer = HumanDeserializer(
                input_file='input/encode_human.json',
                output_file='output/decode_human.json'
            )
        elif kind == 'animal':
            deserializer = AnimalDeserializer(
                input_file='input/encode_animal.json',
                output_file='output/decode_animal.json'
            )

        return deserializer
