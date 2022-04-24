import sys
import os.path
import glob
import re


def main():

    # パラメータ取得
    args = sys.argv
    if 1 == len(args):
        print("Usage " + args[0] + " [FILE PATH]")
        sys.exit()

    # print(args[1])
    # print(os.path.split(args[1]))

    # 初期化
    inputfile = args[1]
    workfile = inputfile + ".work"
    outputfile = inputfile + ".out"

    pattern = r'TCP (Recv|Send) message'

    if True == os.path.isfile(inputfile):
        extractline(pattern, inputfile, workfile)
        shapeline(r'=', r'\t=\t', workfile, outputfile)



def extractline(pattern, inputfile, outputfile):
    # 正規表現パターンコンパイル
    prog = re.compile(pattern)

    with open(outputfile, mode='w', encoding="utf-8") as fo:
        with open(inputfile, encoding="utf-8") as fi:
            datalist = fi.readlines()
            for data in datalist:
                # print(data, end='')
                result = re.match(pattern, data)
                if result: #none以外の場合
                    fo.write(data)


def shapeline(before, after, inputfile, outputfile):
    with open(outputfile, mode='w', encoding="utf-8") as fo:
        with open(inputfile, encoding="utf-8") as fi:
            datalist = fi.readlines()
            for data in datalist:
                result = re.sub(before, after, data)
                if result: #none以外の場合
                    fo.write(result)


main()
