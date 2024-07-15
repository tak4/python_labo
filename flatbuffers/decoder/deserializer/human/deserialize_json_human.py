import base64
import json
import os
import generate.Human.Human


def main():

    with open('./serializer/human/encode_human.json', 'r') as json_file:
        json_data = json.load(json_file)

    buf_encode = json_data['data']
    buf = base64.b64decode(buf_encode)

    human = generate.Human.Human.Human.GetRootAsHuman(buf, 0)

    name = human.Name().decode()
    age = human.Age()
    print(name)
    print(age)

    # dataキーを差し替える
    del(json_data['data'])
    print(json_data)

    json_data['data'] = {name: age}
    print(json_data)

    output_dir = os.path.dirname(__file__)
    output_json = os.path.join(output_dir, 'decode_human.json')
    with open(output_json, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    main()
