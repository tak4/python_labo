# 参照カウントの確認
import sys

x = [1, 2, 3]
# xに代入されているオブジェクトの参照カウント+1が取得される
# +1 なのは、getrefcount()で参照している分
print(f'xの参照カウント : {sys.getrefcount(x) - 1}')
y = x
print(f'xの参照カウント : {sys.getrefcount(x) - 1}')
