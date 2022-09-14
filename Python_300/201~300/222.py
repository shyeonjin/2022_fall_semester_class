def print_score(k):
    total=0
    for i in k:
        total+=i
    total=total/len(k)
    print(total)

print_score([1, 2, 3])