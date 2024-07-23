import os
import pytest
from target.prime import is_prime
from target.calc import add
from target.assert_test import check_param
import target.numbers_sorted

from test_target.utility import Environment

# @pytest.mark.skip(reason="no way of currently testing this")
def test_add():
    answer = add(1, 2)
    assert(answer == 3)

@pytest.mark.skip(reason="no way of currently testing this")
def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)

@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (6, False),
    (7, True),
    (8, False),
    (9, False),
    (10, False),
])
@pytest.mark.skip(reason="no way of currently testing this")
def test_is_prime_parametrize(number, expected):
    assert is_prime(number) == expected

@pytest.mark.skip(reason="no way of currently testing this")
def test_load_numbers_sorted(txt):
    assert target.numbers_sorted.load_numbers_sorted(txt) == [1, 2, 3, 4, 5]

@pytest.mark.skip(reason="no way of currently testing this")
# setting/setting.yaml をテストコードで参照する試み
def test_ref_setting():
    setting = Environment.get_setting()
    print('    {}    '.format(setting['key']), end="")

@pytest.mark.skip(reason="no way of currently testing this")
def test_assert_ok():
    check_param(0)

@pytest.mark.skip(reason="no way of currently testing this")
def test_assert_error():
    try:
        check_param(1)
    except AssertionError as ex:
        print('< {} >'.format(ex), end='')

@pytest.mark.skip(reason="no way of currently testing this")
def test_send(mocker):
    # 工事中
    receive = mocker.patch('studies.interaction.receive')

def test_get_env():
    env = os.getenv('TEST_ENV_TEST')
    print("env=", env)