from itertools import permutations

user_input = list(input())
k = int(input())
# 순열사용
print(max(list(map(''.join, permutations(user_input, k)))))