import pytest
import time
import logging

# pytest.fixtur#
# テスト前後で行いたい処理を記述する
# conftest.pyに定義すると、conftest.py配下のテストに対して有効になる
# autouse=True とすれば、それぞれのテストで関数の指定は不要
# テスト個別に有効化する場合は、テスト関数のパラメータに、
# fixtureの関数名を指定する
# 例：def test_answer(setup):
@pytest.fixture(autouse=False)
def setup():
    # テスト前に処理
    sleep_time = 0.5
    time.sleep(sleep_time)
    yield
    # テスト後に処理
    sleep_time += 0.25
    time.sleep(sleep_time)

    # Logger設定
    logger = logging.getLogger(__name__)
    logger.debug('This message should go to the log file')