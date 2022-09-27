def calc_c(first,second,tool):
    if tool=="+":
        return first+second
    elif tool=="-":
        return first-second
    elif tool=="*":
        return first*second
    else:
        return first/second

with open("calc.txt","r",encoding="UTF-8") as c:
    k=c.readlines()
    for i in k:
        a,b,c=i.split()
        print(calc_c(int(a),int(b),c))
