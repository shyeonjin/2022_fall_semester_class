def solution(n):
    people = 0
    total = 0
    while(True):
        # 가기전의 악수를 센다
        total = people*(people-1)/2
        if n<total:
            break
        people+=1
    # 초과된 악수의 값을 가지고 언제 갔는지 구한다.
    times = int(people-(total-n)-1)
    return [times,people]
print(solution(59))
