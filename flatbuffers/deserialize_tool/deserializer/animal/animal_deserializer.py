import base64
import json

from deserializer.base.deserializer import BaseDeserializer
from deserializer.animal.generated.Animal import Animal

class AnimalDeserializer(BaseDeserializer):

    def __init__(self):
        self.input_file = 'input/encode_animal.json'
        self.output_file = 'output/decode_animal.json'

    def decode(self, input_file=None, output_file=None):
        print('decode')
        if input_file is not None:
            self.input_file = input_file 
        if output_file is not None:
            self.output_file = output_file 
        print(self.input_file)
        print(self.output_file)

        # 入力ファイル
        with open(self.input_file, 'rb') as json_file:
            json_data = json.load(json_file)

        # デシリアライズ
        buf_encode = json_data['data']
        buf = base64.b64decode(buf_encode)

        animal = Animal.GetRootAsAnimal(buf, 0)

        kind = animal.Kind().decode()
        age = animal.Age()
        print(kind)
        print(age)

        # dataキーを差し替える
        del(json_data['data'])
        json_data['data'] = {kind: age}
        print(json_data)

        with open(self.output_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)


    def decode_and_process(self, input_file=None) -> list[str]:
        return None