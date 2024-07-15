import pytest
import requests
import helper.testing_utils
from test_ext_function.utility import Environment

# @pytest.mark.skip(reason="no way of currently testing this")
def test_is_specified_json():
    url = "http://127.0.0.1:5000/case1"
    response = requests.get(url)

    schema = {'name': 'Cannon Wood', 'age': 26}

    # AssertionErrorがraiseされることをテストする
    # raiseされなければエラー
    with pytest.raises(AssertionError, match=r'name error'):
        helper.testing_utils.is_specified_json(response, schema)

@pytest.mark.skip(reason="no way of currently testing this")
def test_generate_bearer_token():
    box = helper.testing_utils.generate_bearer_token()
    print(box)

# @pytest.mark.skip(reason="no way of currently testing this")
def test_response_test():

    setting = Environment.get_setting()
    print('    {}    '.format(setting['key']), end="")

    url = "http://127.0.0.1:5000/case1"
    response = requests.get(url)

    helper.testing_utils.response_test(response)