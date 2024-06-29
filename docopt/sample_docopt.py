# 参考
# https://qiita.com/ymdymd/items/651245d80964393b12c5

"""Overview:
  サブコマンド・オプション・引数をdocoptで受け、keyとvalueを全表示する

Usage:
  docopt_test [-a] [-b|--bbb] [-c...] [<z>...]

Options:
  -a           : 任意オプション(引数なし)  → 有無を示すTrue/False
  -b --bbb     : 任意オプション(引数なし)  → 有無を示すTrue/False
  -c...        : 任意オプション(引数なし)  → 指定回数を示す数値
"""

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__)
    print("  {0:<20}{1:<20}{2:<20}".format("key", "value", "type"))
    print("  {0:-<60}".format(""))
    for k,v in args.items():
        print("  {0:<20}{1:<20}{2:<20}".format(str(k), str(v), str(type(v))))
