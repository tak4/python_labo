import re

# ? : 0, 1回の繰り返し
print('ab?', 'abb')
m = re.match('ab?', 'abb')
print(m)

# * : 0回以上の繰り返し
print('ab*', 'abbb')
m = re.match('ab*', 'abbb')
print(m)

# + : 1回以上の繰り返し
print('ab+', 'abbb')
m = re.match('ab+', 'abbb')
print(m)

# {x} ] 回数指定
print('a{3}', 'aaa')
m = re.match('a{3}', 'aaa')
print(m)

# {x,x} ] 回数指定
print('a{2,4}', 'aaaa')
m = re.match('a{2,4}', 'aaaa')
print(m)

# 集合
print('[a-c]', 'aaaa')
m = re.match('[a-c]', 'aaaa')
print(m)

# \w : [a-zA-Z0-9_]
print('\w', '_')
m = re.match('\w', '_')
print(m)

# \W : [^a-zA-Z0-9_]
print('\W', '@')
m = re.match('\W', '@')
print(m)

# \d : [0-9]
print('\d', '1')
m = re.match('\d', '1')
print(m)

# \d : [^0-9]
print('\D', 'a')
m = re.match('\D', 'a')
print(m)

# | : or 
print('a|b', 'b')
m = re.match('a|b', 'b')
print(m)

# () | 塊
print('(abc)+', 'abcabcabc')
m = re.match('(abc)+', 'abcabcabc')
print(m)

# \s : 空白
print('\s', ' ')
m = re.match('\s', ' ')
print(m)

# \S : 空白以外
print('\S', '1')
m = re.match('\S', '1')
print(m)

# エスケープ
print('\*', '*')
m = re.match('\*', '*')
print(m)

# 先頭にマッチ
print('^abc', 'abctest abc')
m = re.search('^abc', 'abctest abc')
print(m)

# 終端にマッチ
print('abc$', 'abctest abc')
m = re.search('abc$', 'abctest abc')
print(m)
