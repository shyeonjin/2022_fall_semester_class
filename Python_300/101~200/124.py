a,b,c=map(int,input("세 개의 숫자를 입력하세요").split())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)