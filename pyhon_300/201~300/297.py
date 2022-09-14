per = ["10.31", "", "8.00"]


l=[]
for i in per:
    try:
        l.append(float(i))
    except:
        l.append(0)

print(l)