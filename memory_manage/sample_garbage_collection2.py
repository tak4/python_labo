# ガベージコレクションの確認
import sys
import tracemalloc
import gc

tracemalloc.start()

class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.data = [0] * (10**6)

user_1 = User('鈴木')
user_2 = User('田中')
user_2.friends.append(user_1)


ss = tracemalloc.take_snapshot()
# 'filename'でファイルごとのメモリ使用量を取得
for s in ss.statistics('filename'):
    print('前', s)

# ガベージコレクション
print(f'前 user_1の参照カウント : {sys.getrefcount(user_1) - 1}')
del user_1  # user_2からuser_1は参照されているので参照カウントは減らない
# 以降、user_1 は使えない
# print(f'後 user_1の参照カウント : {sys.getrefcount(user_1) - 1}') 
gc.collect()

ss = tracemalloc.take_snapshot()
# 'filename'でファイルごとのメモリ使用量を取得
for s in ss.statistics('filename'):
    print('後', s)


tracemalloc.stop()