n = int(input())
print([i for i in range(2, n + 1) if n % i == 0][0])