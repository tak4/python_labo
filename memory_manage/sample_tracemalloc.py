import tracemalloc

# メモリの追跡を開始
tracemalloc.start()

def foo():
    x = [0] * (10**6)
    y = x
    ss = tracemalloc.take_snapshot()
    # 'filename'でファイルごとのメモリ使用量を取得
    for s in ss.statistics('filename'):
        print('関数内', s)

foo()

ss = tracemalloc.take_snapshot()
# 'filename'でファイルごとのメモリ使用量を取得
for s in ss.statistics('filename'):
    print('関数外', s)

# メモリの追跡を終了
tracemalloc.stop()
