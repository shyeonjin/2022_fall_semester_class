with open("1.txt","r", encoding="utf-8") as k:
    lk=k.readlines()
    l=[]
    for i in lk:
        l.append(i.strip())
    print(l)
