def 함수(a, b) :
    print(a + b)

함수("안녕", 3)
# TypeError: must be str, not int

# 함수가 정수형끼리의 덧셈인데 두 개 중 하나의 인자가 문자형으로 들어왔기에
# 에러가 뜬다.