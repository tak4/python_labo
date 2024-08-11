# content of test_sample.py
def inc(x):
    return x + 1

def test_answer(setup):
    assert inc(4) == 5

# content of test_tmp_path.py
# def test_needsfiles(tmp_path):
#     print(tmp_path)
#     assert 0

