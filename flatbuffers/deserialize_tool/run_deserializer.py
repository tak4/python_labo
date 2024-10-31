from optparse import OptionParser

from creator.deserializer_creator import DesealizeCreator as dc
from creator.deserializer_creator_importlib import DesealizeCreator as dcil

def main():

    # 入力オプションの処理
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-k', '--kind', action='store', type='string',
                      dest='kind', help='kind')
    parser.add_option('-i', '--input', action='store', type='string',
                      dest='input_file', help='input file name')
    parser.add_option('-o', '--output', action='store', type='string',
                      dest='output_file', help='output file name')

    options, args = parser.parse_args()

    # デシリアライズ処理
    call(options.kind, options.input_file, options.output_file)

def call(kind=None, input_file=None, output_file=None):

    # デバッグ：creater切り替え
    # deserializer = dc.create(kind)
    deserializer = dcil.create(kind)

    deserializer.decode(input_file, output_file)
    fl = deserializer.decode_and_process(input_file)
    if fl is not None:
        for v in fl:
            print(v)
    # deserializer = DesealizeCreator.create2(kind)


if __name__ == "__main__":
    main()