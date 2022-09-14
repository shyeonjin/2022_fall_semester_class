put= int(input("솟자를 입력하세요"))
put-=20
if put>255:
    print(255)
elif put<0:
    print(0)

else:
    print(put)