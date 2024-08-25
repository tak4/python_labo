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
    with open(options.input_file, 'rb') as f:
      buf = f.read()
      buf = bytearray(buf)

    # デシリアライズ
    human = Human.GetRootAsHuman(buf, 0)
    name = human.Name().decode()
    age = human.Age()
    print(name)
    print(age)
    
    # 出力ファイル
    with open(options.output_file, 'w') as f:
        f.write(name)
        f.write('\n')
        f.write(str(human.Age()))


if __name__ == '__main__':
    main()
