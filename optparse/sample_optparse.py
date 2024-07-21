from optparse import OptionParser
from optparse import OptionGroup

# optparse
# コマンドラインからのオプション指定を処理するための仕組み
# python sample_optparse.py -h
# python sample_optparse.py -f test.txt
# python sample_optparse.py --file=test.txt
# python sample_optparse.py --file test.txt
# python sample_optparse.py -n 10
# python sample_optparse.py --num=10
# python sample_optparse.py --num 10
# python sample_optparse.py -v
# python sample_optparse.py -e prd
# python sample_optparse.py -e prd --release
# python sample_optparse.py -e develop --release
# python sample_optparse.py -g
def main():
    #
    # optionを追加
    #
    usage = 'usage: %prog [options] arg1 arg2'
    parser = OptionParser(usage=usage)
    parser.add_option('-f', '--file', action='store', type='string',
                      dest='filename', help='File name')
    parser.add_option('-n', '--num', action='store', type='int', dest='num')

    # -v と -q で同じverboseに設定
    # set_defaults()で初期値を設定できる
    parser.set_defaults(verbose=False)
    parser.add_option('-v',  action='store_true', dest='verbose')
    parser.add_option('-q',  action='store_false', dest='verbose')
    parser.add_option('-r', action='store_const', const='root', dest='user_name')

    # callback
    # --release を付けた時、is_release()がCallされて、envが'prd'かどうかチェックされる
    parser.add_option('-e', dest='env')
    def is_release(option, opt_str, value, parser):
        if parser.values.env == 'prd':
            raise parser.error("Can't relase")
        # release に True を設定
        setattr(parser.values, option.dest, True)
    parser.add_option('--release', action='callback', callback=is_release, dest='release')

    # 別グループのoptionを追加
    group = OptionGroup(parser, 'Dangerous options')
    group.add_option('-g', action='store_true', help='Group option')
    parser.add_option_group(group)

    #
    # 入力されたoptionを確認
    #
    options, args = parser.parse_args()

    print(type(options)) # options の型は、<class 'optparse.Values'>
    print(options.filename, options.num)
    print(options)
    print(type(args), args) #   args の型は<class 'list'>

if __name__ == '__main__':
    main()
