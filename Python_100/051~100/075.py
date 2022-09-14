def sol(n):
    n =int(n)
    count = 0
    ck=0

    for i in range(n+1):
        i=str(i)
        for k in range(len(i)):
            if i[k]=="3"or i[k]=="6" or i[k]=="9":
                continue
            else:
                ck=1
        if ck==0:
            count+=1
        ck=0
    return count


n=input()
print(sol(n))