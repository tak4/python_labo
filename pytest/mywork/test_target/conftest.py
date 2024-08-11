import pytest
import os
import time
import shutil
import logging

from test_target.utility import Environment

# setting.yaml を読み込む
# setting.yaml へのパスを本ファイルのパスから一階層上のパスから組み立てる
own_path = __file__
base_path = os.path.dirname(own_path)
base_path = os.path.dirname(base_path)
Environment.read_setting(os.path.join(base_path, 'setting/setting.yaml'))

logging.basicConfig(level=logging.DEBUG)

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
    sleep_time = 1
    time.sleep(sleep_time)
    yield
    # テスト後に処理
    sleep_time += 1
    time.sleep(sleep_time)

@pytest.fixture(autouse=True)
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.debug('This message should go to the log file')

    if os.path.isdir('./mywork/temp_work'):
        shutil.rmtree('./mywork/temp_work')
    os.makedirs('./mywork/temp_work', exist_ok=True)

# pytest.fixtur#
# # def test_load_numbers_sorted(txt):
@pytest.fixture
def txt():
    with open('numbers.txt', 'w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield 'numbers.txt'

    os.remove('numbers.txt')
