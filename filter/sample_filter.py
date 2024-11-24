# 与えられたイテラブル（リスト、タプルなど）から、
# 特定の条件を満たす要素だけを抽出して新しいイテラブルを返す関数

numbers = [1, 2, 3, 4, 5]

# 偶数のみ抽出する関数
def is_even(x):
    return x % 2 == 0

# filter関数を使って偶数のみ抽出
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # 出力: [2, 4]
