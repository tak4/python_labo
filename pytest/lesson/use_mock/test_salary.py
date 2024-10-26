import unittest
from unittest.mock import MagicMock
from unittest import mock

import salary

class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        self.assertEqual(s.calculation_salary(), 101)
        
        # bonus_price() が呼び出されていれば成功
        s.bonus_api.bonus_price.assert_called()
        # bonus_price() が1度だけ呼び出されていれば成功
        s.bonus_api.bonus_price.assert_called_once()
        # bonus_price() がyear=2017指定で呼び出されていれば成功
        s.bonus_api.bonus_price.assert_called_with(year=2017)
        # bonus_price() が1度だけyear=2017指定で呼び出されていれば成功
        s.bonus_api.bonus_price.assert_called_once_with(year=2017)
        # bonus_price()の呼び出し回数を確認
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        
        s.bonus_api.bonus_price = MagicMock(return_value=0)
        # => このやり方はあまり良くない
        #    bonus_priceにmockを設定せずにテストを行ってしまう可能性がある
        
        self.assertEqual(s.calculation_salary(), 100)
        s.bonus_api.bonus_price.assert_not_called()

    # patch書き方１
    @mock.patch('salary.ThirdPartyBunusRestApi.bonus_price', return_value=1)
    def test_calculation_salary_patch1(self, mock_bonus):
        # mock_bonusは、salary.Salary()を生成する前にmockとして利用可能
        s = salary.Salary(year=2017)
        self.assertEqual(s.calculation_salary(), 101)
        mock_bonus.assert_called()

    # patch書き方２
    @mock.patch('salary.ThirdPartyBunusRestApi.bonus_price')
    def test_calculation_salary_patch2(self, mock_bonus):
        # テスト前条件設定
        mock_bonus.return_value = 1

        # テスト
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        # テスト結果チェック
        self.assertEqual(salary_price, 101)
        mock_bonus.assert_called()

    # patch書き方３：mockを使いたくない場合は、withステートメントの外に書く
    def test_calculation_salary_patch_with(self):
        with mock.patch(
            'salary.ThirdPartyBunusRestApi.bonus_price' ) as mock_bonus:
            # テスト前条件設定
            mock_bonus.return_value = 1

            # テスト
            s = salary.Salary(year=2017)
            salary_price = s.calculation_salary()

            # テスト結果チェック
            self.assertEqual(salary_price, 101)
            mock_bonus.assert_called()

    # patch書き方４：patcher
    def setUp(self):
        self.patcher = mock.patch('salary.ThirdPartyBunusRestApi.bonus_price' )
        self.mock_bonus = self.patcher.start()

    def tearDonw(self):
        self.patcher.stop()

    def test_calculation_salary_patch_with_patcher(self):
        self.mock_bonus.return_value = 1

        # テスト
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        # テスト結果チェック
        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    # side_effect
    def test_calculation_salary_patch_side_effect(self):
        # def f(year):
        #     return 1
        # self.mock_bonus.side_effect  = f  # 関数指定

        self.mock_bonus.side_effect  = lambda year: 1   # lambda式利用

        # テスト
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        # テスト結果チェック
        self.assertEqual(salary_price, 101)
        self.mock_bonus.assert_called()

    # side_effect
    def test_calculation_salary_patch_side_effect_raise(self):
        self.mock_bonus.side_effect  = ConnectionRefusedError   # 接続エラー

        # テスト
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        # テスト結果チェック
        self.assertEqual(salary_price, 100)
        self.mock_bonus.assert_called()

    # side_effect
    def test_calculation_salary_patch_side_effect_list(self):
        self.mock_bonus.side_effect  = [
            1,          # テスト１
            2,          # テスト２
            3,          # テスト３
            ValueError  # テスト４
        ]

        # テスト１
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        # テスト結果チェック
        self.assertEqual(salary_price, 101)

        # テスト２
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        # テスト結果チェック
        self.assertEqual(salary_price, 102)

        # テスト３
        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()
        # テスト結果チェック
        self.assertEqual(salary_price, 103)

        # テスト４
        s = salary.Salary(year=200)
        with self.assertRaises(ValueError):
            salary_price = s.calculation_salary()


    # patch書き方５：Classごとmockにする
    # spec=True にすることで、bonus_priceをmockとして扱える
    @mock.patch('salary.ThirdPartyBunusRestApi', spec=True)
    def test_calculation_salary_class(self, mock_rest):
        # mock_restは、<class 'unittest.mock.MagicMock'> で渡される
        print(type(mock_rest))
        mock_rest = mock_rest.return_value
        #  => return_valueで、<class 'unittest.mock.NonCallableMagicMock'> が得られる
        #     NonCallableMagicMockを使用する
        print(type(mock_rest))
        mock_rest.bonus_price.return_value = 1

        s = salary.Salary(year=2017)
        salary_price = s.calculation_salary()

        self.assertEqual(salary_price, 101)
        mock_rest.bonus_price.assert_called()



if __name__ == '__main__':
    unittest.main()