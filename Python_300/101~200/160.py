리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트:
    a=i.split(".")
    if a[1]=="h":
        print(i)
    elif a[1]=="c":
        print(i)