import datetime

def findDay(a, b):
    day = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    return day[datetime.date(2020, a, b).weekday()]


m = int(input())
d = int(input())
if 0<m<13:
    if 0<d<32:
        print(findDay(m, d))
    else:
        print("오류")
else:
    print("오류")