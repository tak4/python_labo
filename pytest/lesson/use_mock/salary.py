import requests

# 3rdパーティ製のボーナス金額を取得するAPIを使うためのクラス
class ThirdPartyBunusRestApi(object):
    def bonus_price(self, year):
        r = requests.get('http://localhost/bonus', params={'year': year})
        return r.json()['price']

# 給与を計算するクラス
class Salary(object):
    def __init__(self, base=100, year=2017):
        self.bonus_api = ThirdPartyBunusRestApi()
        self.base = base
        self.year = year

    def calculation_salary(self):
        bonus = 0
        if self.year < 2020:
            try:
                bonus = self.bonus_api.bonus_price(year=self.year)
            except ConnectionRefusedError:
                bonus = 0
        return self.base + bonus
