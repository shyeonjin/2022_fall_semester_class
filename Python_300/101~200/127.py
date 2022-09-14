put = input("주민등록번호: ")
put=put.split("-")[1]
if put[0]=="1" or put[0]=="3":
    print("남자")
else:
    print("여자")