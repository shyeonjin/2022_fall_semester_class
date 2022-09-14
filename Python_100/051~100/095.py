def solution(stamp,roll):
    
    total=stamp.copy()
    
    for ko in range(roll):
        l=[]
        for i in range(len(stamp)):
            l.append([0]*len(stamp[0]))
        for i in range(len(stamp)):
            for j in range(len(stamp[0])):
                l[j][len(stamp[0])-i-1]=stamp[i][j]
        for i in range(len(stamp)):
            for j in range(len(stamp[0])):
                total[i][j]+=l[i][j]
        stamp=l.copy()
            
    print(total)     



stamp = [
[1,1,1,2],
[2,0,0,0],
[1,1,1,1],
[0,0,0,0]
]

roll = 10
solution(stamp,roll)
#print(solution(stamp,roll))