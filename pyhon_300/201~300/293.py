
import csv
with open("3.csv","w", encoding="cp949") as k:
    writer = csv.writer(k)
    writer.writerow(["종목명", "종목코드", "PER"])
    writer.writerow(["삼성전자", "005930", 15.59])
    writer.writerow(["NAVER", "035420", 55.82])