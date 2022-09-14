
#make_map(4,5,[0,0],[[0,1],[1,1],[2,3],[1,3]])
l=[]
total=[]
n=4
m=5
k=[0,0]
q=[[0,1],[1,1],[2,3],[1,3]]
for i in range(m):
    for j in range(n):
        l.append(0)
    total.append(l)
    l=[]
print(total)
total[k[0]][k[1]]=1
print(total)
for i in range(len(q)):
    total[q[i][0]][q[i][1]]=2
fin_total=[]
total=sum(total, [])
for i in range(m+2):
    for j in range(n+2):
        if i==0 or i==m+1:
            l.append(2)
        else:
            if j==0 or j==n+1:
                l.append(2)
            else:
                l.append(total.pop(0))
    fin_total.append(l)
    l=[]

for i in fin_total:
    print(i)
