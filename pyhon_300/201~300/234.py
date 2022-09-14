def pickup_even(k):
    l=[]

    for i in k:
        if i%2==0:
            l.append(i)

    return l

print(pickup_even([3, 4, 5, 6, 7, 8]))