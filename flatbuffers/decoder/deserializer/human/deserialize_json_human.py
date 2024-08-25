import base64
import json
from optparse import OptionParser

from generated.Human import Human

def main():

    # 入力オプションの処理
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-i', '--input', action='store', type='string',
                      dest='input_file', help='input file name')
    parser.add_option('-o', '--output', action='store', type='string',
                      dest='output_file', help='output file name')

    options, args = parser.parse_args()

    # 入力ファイル
    with open(options.input_file, 'rb') as json_file:
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
    print(json_data)

    json_data['data'] = {name: age}
    print(json_data)

    with open(options.output_file, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)


if __name__ == '__main__':
    main()
