import re

def do_regex():
    # 第1引数が正規表現パターン(検索語句)、第2引数が検索対象
    result = re.match('.*[0-9]', 'hello 1234')
    print(result)
    # <_sre.SRE_Match object; span=(0, 3), match='Hel'>
    print(result.group())

def do_regex_complie():
    # あらかじめ正規表現パターンをコンパイル
    regex = re.compile('[H].+')

    result = regex.match('Hellow python')
    print(result)
    # <_sre.SRE_Match object; span=(0, 3), match='Hel'>
    print(result.group())
