def sol(n,l):
# n:택배원 수, l:택배들
    answer = 0
    man = [0]*n
    while sum(l)!=0:
        for j in range(len(man)):		
            if man[j] == 0 and l:
                man[j]+=l.pop(0)
        man = list(map(lambda x : x-1,man))
        answer+=1
    answer+=max(man)
    return answer
n = 3
l = [1,2,1,3,3,3]


print(sol(n,l))