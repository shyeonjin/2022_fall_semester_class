import datetime
for day in range(5, 0, -1):
    print(datetime.datetime.now()-datetime.timedelta(days=day))