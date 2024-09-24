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
        fieldnames = ['fullpath', 'dlink', 'flink', 'fname_wo_ext', 'datetime']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # ファイルのリスト作成
        for f in fl:
            if os.path.isfile(f):
                dname = os.path.dirname(f)
                bname = os.path.basename(f)
                basename_without_ext = os.path.splitext(bname)[0]
                # ファイル名から日時を取得
                m = p.match(bname)
                dt = None
                if m:
                    dt = m.group()
                # pathをHYPERLINKにする
                dlink = '=HYPERLINK("' + dname  + '")'
                flink = '=HYPERLINK("' + f + '")'
                # csv書き出し
                writer.writerow(
                    {
                        "fullpath": f,
                        "dlink": dlink,
                        "flink": flink,
                        "fname_wo_ext": basename_without_ext,
                        "datetime": dt}
                    )

if __name__ == "__main__":
    main()