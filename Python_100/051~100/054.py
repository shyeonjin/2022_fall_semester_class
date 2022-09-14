put=list(map(int,input().split()))
put=sorted(put)
for i in range(len(put) - 1):
    if put[i]+1 != put[i+1]:
        print('NO')
print("YES")
        
