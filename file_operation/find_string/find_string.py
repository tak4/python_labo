import csv
import re
from optparse import OptionParser
from pathlib import Path


def main():

    # パラメータ指定の準備
    usage = 'usage: %prog [options]'
    parser = OptionParser(usage=usage)
    parser.add_option('-t', '--target', action='store', type='string',
                      dest='target', help='target directory')

    # パラメータの取得
    options, args = parser.parse_args()
    print(options.target)

    # 検索する単語のリストを作成する
    search_word_list = make_search_word_list('keyword_list.csv')

    # 単語のリストを元に指定ディレクトリしたのファイルを検索して結果をcsvファイルに出力する
    create_search_result(options.target if options.target is not None else 'target', search_word_list)


def make_search_word_list(keyword_list_file_name):
    """csvファイルに記載されている検索する単語をリスト化する
    Args:
        csv_file_name (string) : 検索する単語が記述されたcsvファイル
    Returns:
        search_word_list (string) : 検索する単語のリスト
        ※正規表現はコンパイル済みオブジェクトを格納する
    """

    search_word_list = []
    with open(keyword_list_file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # 各列の文字列を取得、単語前後の空白を除去しておく
            flg_regex = row.get('flg_regex', '').strip()
            word = row.get('word', '').strip()

            # 正規表現指定の場合は、compileしておく
            if flg_regex == '0':
                search_word_list.append(word)
            else:
                search_word_list.append(re.compile(word))

    return search_word_list


def create_search_result(target, search_word_list):
    """単語リストのの単語を指定ファイル内で検索し、結果をcsvファイルに出力する
    """

    # Windowsでは、open関数を使ってファイルを開くと、
    # デフォルトでテキストモードになり、改行コードが自動的に変換される
    # その為、newline=""を指定しておく
    with open('keyword_list_result.csv', 'w', newline="") as csvfile:
        # Header作成
        fieldnames = ['file', 'line_no', 'line_string', 'word']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # 指定ディレクトリ以下、指定拡張子のファイルを選択して、単語リストの単語を検索する
        p = Path(target)
        target_file_list = [f for pat in ('*.txt', '*.md', '*.log') for f in p.rglob(pat)]
        for target_file in target_file_list:
            # 1ファイルごとに単語リストの単語を検索する
            result_list = search_words(target_file, search_word_list)

            # 単語の検索結果をcsvファイルへ出力する
            for result in result_list:
                writer.writerow(
                    {
                        fieldnames[0]: result[0],
                        fieldnames[1]: result[1],
                        fieldnames[2]: result[2],
                        fieldnames[3]: result[3]
                    }
                )
                print(fieldnames, result)


def search_words(file_name, search_word_list):
    """検索対象のファイルをリストで指定された単語で検索して一致した行をリストへ出力する
    Args:
        file_name (string) : 検索対象を行うファイル名
        search_word_list (list) : 検索文字列のリスト ※正規表現はcompile済みオブジェクト
    Returns:
        result_list (list) : 検索した結果、マッチした行の文字列のリスト
    """

    search_result_list = []
    with open(file_name, 'r') as f:
        for line_no, line in enumerate(f):
            line_string = line.rstrip('\r\n')
            if not line_string:    # 空行Skip
                continue
            for word in search_word_list:
                if isinstance(word, re.Pattern):
                    if word.match(line_string):
                        search_result_list.append((str(file_name), line_no+1, line_string, str(word))) 
                else:
                    if word in line_string:
                        search_result_list.append((str(file_name), line_no+1, line_string, str(word))) 

    return search_result_list


if __name__ == "__main__":
    main()
