def rule(n):
    num_l = max([int(i) for i in n])
    d = [str(i)+str(str(n).count(str(i))) for i in range(1,num_l+1)]
    return ''.join(d)



put=int(input())
start="1"
if put==1:
    print("1")
else:
    for i in range(1,put):
        start=rule(start)


    print(start)

