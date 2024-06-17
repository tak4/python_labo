import pytest
import requests
import sys
import helper.testing_utils

@pytest.mark.skip(reason="no way of currently testing this")
def test_is_specified_json():
    box = helper.testing_utils.generate_bearer_token()
    print(box)

def test_response_test():

    url = "http://127.0.0.1:5000/items"
    response = requests.get(url)
    # response = requests.models.Response()

    helper.testing_utils.response_test(response)