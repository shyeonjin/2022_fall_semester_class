a=list(input().split())
b=list(map(int,input().split()))
c=[]
d={}
for i in range(len(a)):
    c.append([a[i],b[i]])
c=sorted(c,key= lambda c: c[1], reverse=True)
for i in range(len(c)):
    d[c[i][0]] = i+1
print(d)