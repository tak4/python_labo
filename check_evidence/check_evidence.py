import csv
import glob
from optparse import OptionParser
import os
import re

def main():
    # 入力オプションの処理
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-i', action='store', type='string',
                      dest='input_path', help='input path')
    options, args = parser.parse_args()

    # glob
    target_path = os.path.join(options.input_path, '**')
    fl = glob.glob(target_path, recursive=True)

    # re：日時
    p = re.compile('[0-9]{14}')

    # Windowsでは、open関数を使ってファイルを開くと、
    # デフォルトでテキストモードになり、改行コードが自動的に変換される
    # その為、newline=""を指定しておく
    with open('evidence_list.csv', 'w', newline="") as csvfile:
        # Header作成
        fieldnames = ['path', 'link', 'datetime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # ファイルのリスト作成
        for f in fl:
            if os.path.isfile(f):
                # ファイル名から日時を取得
                m = p.match(os.path.basename(f))
                dt = None
                if m:
                    dt = m.group()
                # pathをHYPERLINKにする
                link = '=HYPERLINK("' + f + '")'
                # csv書き出し
                writer.writerow({"path": f, "link": link, "datetime": dt})

if __name__ == "__main__":
    main()