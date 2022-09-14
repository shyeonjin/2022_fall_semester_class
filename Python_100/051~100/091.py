import random  as r

score = []
class_score = []
total_score = []
for j in range(30):
    for k in range(7):
        for i in range(5):
            score.append(r.randint(1, 100))
        class_score.append(score)
        score=[]
    total_score.append(class_score)
    class_score=[]


total_average = 0
c_average = []
s_average = 0
for c in total_score:
    for s in c:
        s_average += sum(s)/5
    c_average.append(s_average // 30)
    s_average = 0

print(c_average)
print(sum(c_average)//len(c_average))