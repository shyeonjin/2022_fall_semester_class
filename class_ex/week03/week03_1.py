import math
def changenum(k):
    g=1/(1+math.e**(-k))
    return g*(1-g)


put=int(input("입력하세요:"))
print(changenum(put))