def print_mxn(a,num):
    long=int(len(a)/num)
    for i in range(long+1):
        print(a[i*num:i*num+num])

print_mxn("아이엠어보이유알어걸", 3)