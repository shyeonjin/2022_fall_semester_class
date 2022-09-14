def merge_sort(k):
    long = len(k)
    if long <= 1:
        return k
    mid = long // 2
    group_one = merge_sort(k[:mid])
    group_two = merge_sort(k[mid:])
    result = []

    while group_one and group_two:
        if group_one[0] < group_two[0]:
            result.append(group_one.pop(0))
        else:
            result.append(group_two.pop(0))

    while group_one:
        result.append(group_one.pop(0))
    while group_two:
        result.append(group_two.pop(0))
    return result

l = input().split(' ')
l = [int(i) for i in l]

print(merge_sort(l))