import base64
import json

from deserializer.base.deserializer import BaseDeserializer
from deserializer.human.generated.Human import Human

class HumanDeserializer(BaseDeserializer):

    def decode(self):
        print('decode')
        print(self.input_file)
        print(self.output_file)

        # 入力ファイル
        with open(self.input_file, 'rb') as json_file:
            json_data = json.load(json_file)

        # デシリアライズ
        buf_encode = json_data['data']
        buf = base64.b64decode(buf_encode)

        human = Human.GetRootAsHuman(buf, 0)

        name = human.Name().decode()
        age = human.Age()
        print(name)
        print(age)

        # dataキーを差し替える
        del(json_data['data'])
        json_data['data'] = {name: age}
        print(json_data)

        with open(self.output_file, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
