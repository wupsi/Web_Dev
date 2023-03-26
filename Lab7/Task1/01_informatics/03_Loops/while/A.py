n, i = int(input()), 1
while i <= n:
    if int(i ** 0.5) * int(i ** 0.5) == i:
        print(i)
    i += 1