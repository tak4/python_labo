import os
import sys
from pathlib import Path


def main():
    if len(sys.argv) <= 1:
        print('please specify input filename')
        return    

    # 入力ファイルの絶対パスを取得
    input_abs_file_name = os.path.abspath(sys.argv[1])
    # 出力ファイル名を作成する為に、パスとファイル名に分割
    dir_name, file_name = os.path.split(input_abs_file_name)
    output_filename = os.path.join(dir_name, 'output_' + file_name)

    with open(sys.argv[1], 'r') as fi:
        read_buffer = fi.read()
        with open(output_filename, 'w') as fo:
            fo.write(read_buffer)

if __name__ == "__main__":
    main()