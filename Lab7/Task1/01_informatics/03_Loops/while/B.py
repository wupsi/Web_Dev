n, i = int(input()), 2
while i <= n:
    if not n % i:
        print(i)
        break
    i += 1