import base.deserializer_creator 
from deserializer.human.human_deserializer import HumanDeserializer

class HumanDeserializerCreater(base.deserializer_creator.DeserilizerCreator):

    def create(self):
        return HumanDeserializer()
