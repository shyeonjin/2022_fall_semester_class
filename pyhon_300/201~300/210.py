def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

# 함수 3호출 for문안에 함수2호출을 for문 3번
# BCBCBC 그리고 함수1 A
# 결과
"""
B
C
B
C
B
C
A
"""