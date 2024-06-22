import datetime

# フォーマット文字列
format = "%Y%m%d%H%M%S%f"
# 文字列の日付
date_str = "20240605062250123"
# datetime型に変換
dt1 = datetime.datetime.strptime(date_str, format)

print('--- 初期状態 ---')
# datetime出力
# タイムゾーン未設定 -> naive
print('timezone  : {} / {}'.format(dt1.tzinfo, type(dt1.tzinfo)))
print('datetiome : {} / {}'.format(dt1, type(dt1)))

# タイムゾーン設定 -> aware
print()
print('- replace timezone=utc -')
dt_replace_tz_utc = dt1.replace(tzinfo=datetime.timezone.utc)
print('timezone  : {} / {}'.format(dt_replace_tz_utc.tzinfo, type(dt_replace_tz_utc.tzinfo)))
print('datetikme : {} / {}'.format(dt_replace_tz_utc, type(dt_replace_tz_utc)))
print()

print('--- datetime -> Unix time ---')
# datetime -> Unix time
# timestamp()
# Unix time(=POSIX タイムスタンプ) : 協定世界時 (UTC) 1970年1月1日午前0時0分0秒から経過した秒数

#   datetime インスタンスに対応する POSIX タイムスタンプを返す
#   timestamp()では、datetimeがnaive(タイムゾーンが未設定)ならdatetimeはローカル時刻(Tokyo/Japan)として扱われる
#   よって、timestamp() は datetimeに対して -9h した秒数を返す
dt_to_timestamo = dt1.timestamp()
print('timestamp (tz=None) : {} / {}'.format(dt_to_timestamo, type(dt_to_timestamo)))

#   datetime インスタンスに対応する POSIX タイムスタンプを返す
#   timestamp()では、datetimeがaware(タイムゾーンが設定されている)ならdatetimeは設定されたタイムゾーン(=UTC)が効く
#   よって、timestamp() は datetimeに対して +-0h した秒数を返す
dt_to_timestamo_utc = dt_replace_tz_utc.timestamp()
print('timestamp (tz=UTC)  : {} : {}'.format(dt_to_timestamo_utc, type(dt_to_timestamo_utc)))
print('  -> timestamp (tz=UTC) - timestamp (tz=None) = {}'.format(dt_to_timestamo_utc-dt_to_timestamo))  # 差は9h (=3600*9=32400)
print()

# datetime -> Unix time
print('--- Unix time -> datetime ---')
# Unix time -> datetime
# fromtimestamp()

#   タイムゾーンを指定しない場合、POSIX タイムスタンプに対応するローカルな日付を返す。
#   つまり、fromtimestamp()では、入力されたPOSIX タイムスタンプに対して、+9hされたdatetimeが返される。
timestamp_to_dt = datetime.datetime.fromtimestamp(dt_to_timestamo)
print('timestamp (tz=None) to datetime      : {} / {}'.format(timestamp_to_dt, type(timestamp_to_dt)))  # dt_to_timestamo+9h

#   タイムゾーンを指定する場合、指定されたタイムゾーンでタイムスタンプは変換される
#   つまり、fromtimestamp()では、入力されたPOSIX タイムスタンプに対して、+-0hされたdatetimeが返される。
timestamp_to_dt_utc = datetime.datetime.fromtimestamp(dt_to_timestamo, tz=datetime.timezone.utc)  # dt_to_timestamo+0h
print('timestamp (tz=None) to datetime(UTC) : {} / {}'.format(timestamp_to_dt_utc, type(timestamp_to_dt_utc)))

#   タイムゾーンを指定しない場合、POSIX タイムスタンプに対応するローカルな日付を返す。
#   つまり、fromtimestamp()では、入力されたPOSIX タイムスタンプに対して、+9hされたdatetimeが返される。
timestamp_utc_to_dt = datetime.datetime.fromtimestamp(dt_to_timestamo_utc)  # dt_to_timestamo_utc+9h
print('timestamp (tz=UTC) to datetime       : {} / {}'.format(timestamp_utc_to_dt, type(timestamp_utc_to_dt)))
print()

print('--- replace month ---')
# 月を変更
dt_replace_month = dt1.replace(month=7)
print('timezone  : {} / {}'.format(dt_replace_month.tzinfo, type(dt_replace_month.tzinfo)))
print('datetime  : {} / {}'.format(dt_replace_month, type(dt_replace_month)))
print()

print('--- now ---')
dt_now = datetime.datetime.now()
print('timezone (tz=None) : {} / {}'.format(dt_now.tzinfo, type(dt_now.tzinfo)))
print('datetime (tz=None) : {} / {}'.format(dt_now, type(dt_now)))
dt_now_utc = datetime.datetime.now(datetime.timezone.utc)
print('timezone (tz=UTC)  : {} / {}'.format(dt_now_utc.tzinfo, type(dt_now_utc.tzinfo)))
print('datetime (tz=UTC)  : {} / {}'.format(dt_now_utc, type(dt_now_utc)))
