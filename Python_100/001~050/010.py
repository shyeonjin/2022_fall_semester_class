def star(a):
    i=0
    while i<a:
        if i<a:
            k=0
            while k<4-i:
                print(' ' ,end='')
                k+=1
            k=0
            while k<i*2+1:
                print('*' , end='')
                k+=1
        print()
        i+=1
a=int(input("입력:"))
star(a)