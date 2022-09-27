# 1부터 1000까지의 자연수 중 3으의 배수의 총합
total=0
for i in range(1,1001):
    if i%3==0:
        total+=i

print(total)