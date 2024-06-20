import datetime

# フォーマット文字列
format = "%Y%m%d%H%M%S%f"
# 文字列の日付
date_str = "20240605062250123"
# datetime型に変換
dt = datetime.datetime.strptime(date_str, format)

print(type(dt), dt)
print(dt.tzinfo)
dt.replace(tzinfo=datetime.timezone.utc)
print(type(dt), dt)
print(dt.tzinfo)
print(type(datetime.timezone.utc), datetime.timezone.tzname)


now = datetime.datetime.now()
print(now, now.tzinfo)



# datetime -> 小数
dt_timestamo = dt.timestamp()
print(type(dt_timestamo), dt_timestamo)

# 小数 -> datetime
dt2 = datetime.datetime.fromtimestamp(dt_timestamo)
print(type(dt2), dt2)
print(dt2.tzinfo)
