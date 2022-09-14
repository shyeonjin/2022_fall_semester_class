with open("2.txt","r", encoding="utf-8") as k:
    lk=k.readlines()
    d={}
    for i in lk:
        z,x=(i.strip()).split()
        d[z]=x
    print(d)
