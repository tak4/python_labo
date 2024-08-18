import os
import pytest
import calculation
import shutil

is_release = True

class TestCal(object):
    # クラス単位のsetup
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'

    # クラス単位のteardown
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    # テスト単位のsetup
    def setup_method(self, method):
        print('method={}'.format(method.__name__))

    # テスト単位のteardown
    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_add_num_and_double(self):
        assert self.cal.add_num_and_double(1, 1) == 4

    # fixture : request パラメータを受け取る
    # pytest -s --os-name=mac
    def test_add_num_and_double_fixture_request(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(
            self.test_dir,
            self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

    # fixture : tmpdir利用
    def test_save(self, tmpdir):
        print(tmpdir)
        self.cal.save(tmpdir, self.test_file_name)
        # self.cal.save('./tmpdir', self.test_file_name)  #tmpdirを使用しない
        test_file_path = os.path.join(
            tmpdir, self.test_file_name
        )
        assert os.path.exists(test_file_path) is True

    # fixture : 独自fixture利用
    def test_add_num_and_double_my_fixture(self, csv_file):
        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip')
    # @pytest.mark.skipif(is_release == True, reason='skip')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
