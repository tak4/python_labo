import csv
import glob
import os
import sys
import re

def main():

    if len(sys.argv) <= 1:
        print('no input file...')
        sys.exit()

    input_path = sys.argv[1]
    target_path = os.path.join(input_path, '**')
    file_path_list = glob.glob(target_path, recursive=True)

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
        for f in file_path_list:
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