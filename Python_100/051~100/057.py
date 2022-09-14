def count(n):
	countN = str(list(range(n+1))).count('1')
	return countN

print(count(1000))