import datetime

x = datetime.datetime.now()
print(x)
print(x.strftime("%H:%M:%S"))
#TODO: timedelta
y = datetime.datetime(1994, 6, 19)
diff = x - y

# timedelta read-only attribute, method
print(diff.days)
print(diff.total_seconds())
# 時間區段 1天
gap = datetime.timedelta(1)
print(x + gap)#明天時間