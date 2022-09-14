put=int(input())
count=0
for i in range(2,put):
    if put%i==0:
        count=1
if put>1:
    if count==0:
        print("YES")
    else:
        print("NO")

else:
    print("NO")