put=input()
count=0
s=""
k=put[0]
for i in put:
    if i == k:
        count+=1
    else:
        s+=k+str(count)
        k=i
        count=1
s+=k+str(count)
print(s)
