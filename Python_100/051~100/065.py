a = [1,2,3,4]
b = ['a','b','c','d']
k=[]
z=[]
for i in range(len(a)):
    if i%2==0:
        k.append(a[i])
        k.append(b[i])
        z.append(k)
    else:
        k.append(b[i])
        k.append(a[i])
        z.append(k)
    k=[]
print(z)
