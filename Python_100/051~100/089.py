
#(4,5,[0,0],[[0,1],[1,1],[2,3],[1,3]])



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
clk=[2,2,2,4,4,4]
print("캐릭터 이동전")
for i in fin_total:
    print(i)
while True:
    
    a=k[0]+1
    b=k[1]+1

    for i in clk:
        
        if i==1:
            if fin_total[a-1][b]==2:
                pass
            else:
                fin_total[a-1][b]=1
                fin_total[a][b]=0
                a-=1
                

        elif i==2:
            if fin_total[a+1][b]==2:
                pass
            else:
                fin_total[a+1][b]=1
                fin_total[a][b]=0
                a+=1

        elif i==3:
            if fin_total[a][b-1]==2:
                pass
            else:
                fin_total[a][b-1]=1
                fin_total[a][b]=0
                b-=1

        elif i==4:
            if fin_total[a][b+1]==2:
                pass
            else:
                fin_total[a][b+1]=1
                fin_total[a][b]=0
                
                b+=1
    break
print("캐릭터이동후")          
for i in fin_total:
    print(i)
