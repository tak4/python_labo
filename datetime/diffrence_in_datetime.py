import datetime

# 現在
now = datetime.datetime.now()
print(now)

# １週間前
d = datetime.timedelta(weeks=-1)
print(now + d)
