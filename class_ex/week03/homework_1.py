with open("sales.txt","r",encoding="UTF-8") as o:
    k=o.readlines()
    total=0
    num=0
    for i,a in enumerate(k):
        total+=int(a)
        num=i
with open("summary.txt","w",encoding='UTF-8') as x:
    x.write("총매출:{}\n".format(total))
    x.write("평균일매출:{}\n".format((total/(num+1))))

