import sys
import os.path
import glob
import re


def main():
    val_list = []

    # パラメータ取得
    args = sys.argv
    if 1 == len(args):
        print("Usage " + args[0] + " [FILE PATH]")
        sys.exit()

    # r'' RAW文字列
    # https://sakura-editor.github.io/bbslog/sf/general/3742.html#3757
    re_str_struct = r'struct\s*\S*\s*{([^{}]*({[^{}]*}[^{}]*)*[^{}]*)}\s*\S*\s*;'
    re_str_val = r'(?P<type>\S+)\s+(?P<valname>\S+);'
    # prog = re.compile(pattern)

    f = open(args[1], 'r', encoding='UTF-8')

    data = f.read()
    # print(data)

    result = re.search(re_str_struct, data)
    if result: #none以外の場合
        st_block = result.group(1)
        print(st_block)
        for m in re.finditer(re_str_val, st_block, re.MULTILINE):
            val_list.append((m.group('type'),m.group('valname')))

    # for m in re.finditer(pattern, data, re.MULTILINE):
    #     # print(m.groups())
    #     # print(m.group(0))    # 全体
    #     # print(m.group(1)) 
    #     # print(m.group(2)) 
    #     print(m.group('type')) 
    #     print(m.group('valname'))        

    f.close()

    for v in val_list:
        print(v)


main()
