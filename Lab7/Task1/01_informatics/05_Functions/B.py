def power(a, n):
	k = 1
	for _ in range(int(n)):
		k *= a
	return k

a, n = map(float, input().split())
print(power(a, n))