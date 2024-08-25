from deserializer.human.human_deserializer import HumanDeserializer

class DesealizeCreator(object):

    @classmethod
    def create(cls, kind):

        deserializer = None
        if kind == 'human':
            deserializer = HumanDeserializer(
                input_file='input/encode_human.json',
                output_file='output/decode_human.json'
            )

        return deserializer
