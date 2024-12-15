import re
"""
match()     文字列の先頭で正規表現とマッチするか判定
search()    文字列を走査して、正規表現がどこにマッチするか調べる
findall()   正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditer()  重複しないマッチオブジェクトのイテレータを返す
"""

# match
# 先頭でマッチするか調べる
print('--- search ---')
m = re.match('a.c', 'aecabc')
print(type(m), m)    # マッチオブジェクトが返る
if m is not None:
    print(m.span())     # 何文字目から何文字目にマッチ
    print(m.group())

# search
# 先頭でなくてもマッチするか調べる(１つだけ)
print('--- search ---')
m = re.search('a.c', 'test abc test abc')
print(type(m), m)    # マッチオブジェクトが返る
if m is not None:
    print(m.span())     # 何文字目から何文字目にマッチ
    print(m.group())

# findall
# 複数件マッチするかを調べる
print('--- findall ---')
m = re.findall('a.c', 'test abc test abc')
print(type(m), m)    # リストオブジェクトが返る

# finditer
print('--- finditer ---')
m = re.finditer('a.c', 'test abc test abc')
print([w.group() for w in m])
