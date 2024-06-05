from box import Box

# Box オブジェクトの作成
box = Box(name="Taro", age=30)

# 値の取得と設定
print(box.name)  # Taro
box.age = 31
print(box.age)  # 31

# キーの存在確認
print("name" in box)  # True
print("address" in box)  # False

# キーの削除
# del box.age
# print(box.age)  # KeyError: 'age'

# 要素のイテレーション
for key, value in box.items():
  print(f"{key}: {value}")

# 辞書への変換
dictionary = dict(box)
print(dictionary)  # {'name': 'Taro'}
