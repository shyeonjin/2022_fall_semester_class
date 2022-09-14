put=input()
l=[]
for i in put:
    if i.islower():
        l.append(i.upper())
    else:
        l.append(i.lower())
	
for i in l:
	print(i, end='')