from creator.deserializer_creator import DesealizeCreator

def main():
    call()

def call():
    deserializer = DesealizeCreator.create('human')
    deserializer.decode()

if __name__ == "__main__":
    main()