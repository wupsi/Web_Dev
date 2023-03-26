n = int(input())
inp = list(map(int, input().split()))
print(len([i for i in range(1, len(inp) - 1) if inp[i - 1] < inp[i] > inp[i + 1]]))