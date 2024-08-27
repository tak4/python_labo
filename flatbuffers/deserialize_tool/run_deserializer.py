from optparse import OptionParser

from creator.deserializer_creator import DesealizeCreator

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

    deserializer = DesealizeCreator.create(kind)
    deserializer.decode(input_file, output_file)

if __name__ == "__main__":
    main()