l = [10, 20, 25, 27, 34, 35, 39]
n = int(input('순회 횟수는 :'))
def rotate(inL, inN):
    a=inL.copy()
    b=[]
    for i in range(inN):
        a.insert(0,a.pop())
    for i,j in zip(inL,a):
        b.append(abs(i-j))
    index = b.index(min(b))
    print("index :",index)
    print("value :",inL[index],a[index])

rotate(l,n)