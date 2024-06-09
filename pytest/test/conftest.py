import pytest
import time
import logging

# テスト前後で行いたい処理を記述する
# conftest.pyに定義すると、conftest.py配下のテストに対して有効になる
# autouse=True とすれば、それぞれのテストで関数の指定は不要
@pytest.fixture(autouse=False)
def setup():
    # テスト前に処理
    sleep_time = 0.5
    time.sleep(sleep_time)
    yield
    # テスト後に処理
    sleep_time += 0.25
    time.sleep(sleep_time)

    logger = logging.getLogger(__name__)
    logger.debug('This message should go to the log file')