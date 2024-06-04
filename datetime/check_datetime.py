import datetime

# フォーマット文字列
format = "%Y%m%d%H%M%S%f"

# 文字列の日付
date_str = "20240605062250123"

# datetime型に変換
dt = datetime.datetime.strptime(date_str, format)

# 結果を出力
print(dt)