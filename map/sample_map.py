# リストの各要素を2倍にする
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print(result)   # <map object>
print(list(result))  # [2, 4, 6, 8, 10]

# 文字列のリストを大文字に変換する
words = ['apple', 'banana', 'cherry']
result = map(str.upper, words)
print(result)   # <map object>
print(list(result))  # ['APPLE', 'BANANA', 'CHERRY']

# 複数のリストを同時に処理する
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(result)   # <map object>
print(list(result))  # [5, 7, 9]

