put = input("우편번호: ")
put =put[:3]
if put in ["010", "011", "012"]:
    print("강북구")
elif put in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")