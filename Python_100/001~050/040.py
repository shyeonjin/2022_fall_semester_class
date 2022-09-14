we=int(input()) # 제한몸무게
count=0
num=int(input()) # 친구 수
# 친구들의 몸무게는 무작위
# 두명이상의 친구들과 탄다.
total=0
for i in range(num):
    anrp=int(input("몸무게:"))
    total+=anrp
    if total<=we:
        count+=1
print(count)
