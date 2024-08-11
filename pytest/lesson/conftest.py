import os
import pytest

# 独自fixture
# 独自fixtureに標準？fixture(tmpdir)を付けることもできる
@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')    # テスト前に実行
        yield c
        print('after test')     # テスト後に実行
    return 'csv file!!!'

def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')

