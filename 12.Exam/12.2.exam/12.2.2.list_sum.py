L = list(map(int, input().split()))
M = list(map(int, input().split()))

print(' '.join([str(x + y) for x, y in zip(L, M)]))
