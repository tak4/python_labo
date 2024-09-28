import base64
import flatbuffers
import json
import os
from deserializer.animal.generated import Animal

def main():    
    # バッファーの初期サイズ0
    # 必要に応じて拡張されるらしい
    builder = flatbuffers.Builder(0)

    # 文字列データの生成
    name = builder.CreateString('Dog')

    # Animal Serialize
    Animal.AnimalStart(builder)
    Animal.AnimalAddKind(builder, name)
    Animal.AnimalAddAge(builder, 5)
    animal = Animal.AnimalEnd(builder)
    builder.Finish(animal)

    # Output the buffer data
    buf = builder.Output()

    # Write the binary data to a file
    output_dir = os.path.dirname(__file__)
    output_bin = os.path.join(output_dir, 'output_animal.bin')
    with open(output_bin, 'wb') as f:
        f.write(buf)

    # base64エンコード
    encord_bytes = base64.b64encode(buf)  # base64エンコードして、bytes型を返す
    base64s = encord_bytes.decode() # str型に変換

    # json 出力
    json_data = {'data': base64s}

    output_dir = os.path.dirname(__file__)
    output_json = os.path.join(output_dir, 'encode_animal.json')
    with open(output_json, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
   main()
