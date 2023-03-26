def minOfTwo(a, b):
    return a if a < b else b

a, b, c, d = map(int, input().split())
print(minOfTwo(minOfTwo(a, b), minOfTwo(c, d)))