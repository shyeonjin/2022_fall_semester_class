def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

# 결과 28
# 함수2에 12를 함수1에 대입 14를 함수0에 대입 28 