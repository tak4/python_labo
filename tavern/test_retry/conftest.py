import pytest
import time

# テスト前後で行いたい処理を記述する
# conftest.pyに定義すると、conftest.py配下のテストに対して有効になる
# autouse=True とすれば、それぞれのテストで関数の指定は不要
@pytest.fixture(autouse=True)
def setup():
    # テスト前に処理
    print('----- setup -----')
    sleep_time = 0.125
    time.sleep(sleep_time)
    yield
    # テスト後に処理
    print('----- tear down -----')
    sleep_time += 0.25
    time.sleep(sleep_time)

