def quick_sort(k):
    long = len(k)
    if long <= 1:
        return k
    a = k.pop(long//2)
    group = []
    group_two = []
    
    for i in range(long-1):
        if k[i] < a:
            group.append(k[i])
        else:
            group_two.append(k[i])
    return quick_sort(group) + [a] + quick_sort(group_two)

l = input().split(' ')
l = [int(i) for i in l]

print(quick_sort(l))