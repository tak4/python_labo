import os
from optparse import OptionParser


def main():
    # 入力オプションの処理
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-d', action='store_true',
                      dest='is_lf', help='change lf')
    parser.add_option('-c', action='store_true',
                      dest='is_crlf', help='change crlf')
    parser.add_option('-t', action='store', type='string',
                      dest='target_dir', help='target_dir')
    parser.add_option('-x', action='store', type='string',
                      dest='extension', help='extension')

    options, args = parser.parse_args()

    print(options.is_lf)
    print(options.is_crlf)
    print(options.target_dir)
    print(options.extension)


    new_line_code = '\n'
    if options.is_lf:
        new_line_code = '\n'
    elif options.is_crlf:
        new_line_code = '\r\n'

    change_line_ending(
        new_line_code,
        options.target_dir,
        options.extension
    )


def change_line_ending(new_line_code, target_dir, extension):
    for foldername, subfolders, filenames in os.walk(target_dir):
        for filename in filenames:
            if filename.endswith('.{}'.format(extension)):
                filepath = os.path.join(foldername, filename)
                print(filepath)
                with open(filepath, 'r') as file:
                    content = file.read()
                with open(filepath, 'w', newline=new_line_code) as file:
                    file.write(content)

if __name__ == "__main__":
    main()