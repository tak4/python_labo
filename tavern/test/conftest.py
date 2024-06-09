import pytest
import time
from logging import config
import yaml
import logging

# テスト前後で行いたい処理を記述する
# conftest.pyに定義すると、conftest.py配下のテストに対して有効になる
# autouse=True とすれば、それぞれのテストで関数の指定は不要
@pytest.fixture(autouse=True)
def setup():
    with open("./log_setting/config.yaml", "r") as log_spec_file:
        config.dictConfig(yaml.load(log_spec_file, Loader=yaml.Loader))

    # numeric_level = getattr(logging, 'DEBUG', None)
    # logging.basicConfig(filename='example.log', encoding='utf-8', level=numeric_level)
    # logger = logging.getLogger(__name__)
    # logger.info('So should this')

    # テスト前に処理
    sleep_time = 0.125
    time.sleep(sleep_time)
    yield
    # テスト後に処理
    sleep_time += 0.25
    time.sleep(sleep_time)



@pytest.fixture
def txt() -> str:
    with open('numbers.txt', 'w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield 'numbers.txt'