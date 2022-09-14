def print_5xn(k):
    long=int(len(k)/5)
    for i in range(long+1) :
        print(k[i*5:i*5+5])


print_5xn("아이엠어보이유알어걸")