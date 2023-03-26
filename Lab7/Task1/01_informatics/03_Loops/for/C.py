print(*[i for i in range(int(input()), int(input()) + 1) 
        if int(i ** 0.5) * int(i ** 0.5) == i])