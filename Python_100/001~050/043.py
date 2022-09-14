put=int(input())
l=[]
while put:
    l.append(str(put%2))
    put=int(put/2)
l.reverse()
print(''.join(l))

