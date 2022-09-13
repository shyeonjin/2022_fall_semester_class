money= {"달러": 1167,"엔": 1.096,"유로": 1268,"위안": 171}
user = input("입력: ")
a,b= user.split()
print(float(a) * money[b], "원")