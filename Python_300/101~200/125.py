number = input("휴대전화 번호 입력: ")
num = number.split("-")[0]
if num == "011":
    print("당신의"+" SKT "+"사용자입니다.")
elif num == "016":
    print("당신의"+" KT "+"사용자입니다.")
elif num == "019":
    print("당신의"+" LGU 1"+"사용자입니다.")
else:
    print("알수없음")