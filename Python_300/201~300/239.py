def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 결과 16
# 함수2에서 함수1에 12를 넣어 함수 1에서 16으로 리턴