import re

# スペースで分割する
s = 'My name is ... Mike'
print(s.split())

# \W [^a-zA-Z0-9_] で分割する
p = re.compile(r'\W+')
print(p.split(s))

# 置換
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes'))
# count指定：１つだけ置換する
print(p.sub('colour', 'blue socks and red shoes', count=1))
# 置換した数を合わせて知る tupleで返される
print(p.subn('colour', 'blue socks and red shoes'))

# 置換２
# 置換内容を関数で指定する

# 10進数を16進数に変換する
def hexrepl(match):
    value = int(match.group())
    return hex(value)

# 数字にマッチ
p = re.compile(r'\d')

# sub() に置換処理を行う関数を渡す
print(p.sub(hexrepl, '12345 55 11 test test2'))
