# ガベージコレクションの確認
import tracemalloc
import gc

# メモリの追跡を開始
tracemalloc.start()

def foo():
    x = [0] * (10**6)

    # <xを使った処理>

    ss = tracemalloc.take_snapshot()
    # 'filename'でファイルごとのメモリ使用量を取得
    for s in ss.statistics('filename'):
        print('前', s)

    # ガベージコレクション
    del x
    gc.collect()

    ss = tracemalloc.take_snapshot()
    # 'filename'でファイルごとのメモリ使用量を取得
    for s in ss.statistics('filename'):
        print('後', s)

    y = [1] * (10**6)
    # <yを使った処理>

foo()

# メモリの追跡を終了
tracemalloc.stop()
