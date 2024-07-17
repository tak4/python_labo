from base.deserializer_creator import DeserilizerCreator
from deserializer.human.human_deserializer_creator import HumanDeserializerCreater

def main():
    call()

def call():
    creator = HumanDeserializerCreater()
    deserializer = creator.create()
    deserializer.decode()

if __name__ == "__main__":
    main()