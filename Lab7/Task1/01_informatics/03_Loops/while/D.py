n, i = int(input()), 1
while i <= n:
    if n == i:
        print('YES')
        exit()
    i *= 2

print('NO')