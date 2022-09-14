a=[]
data = [[ 2000,  3050,  2050,  1980],[ 7500,  2050,  2050,  1980],[15450, 15050, 15550, 14900]]
for i in data:
    b=[]
    for j in i:
        b.append(j * 1.00014)
    a.append(b)

print(a)