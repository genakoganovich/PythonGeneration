m, p, n = map(int, [input() for _ in range(3)])

size = m

for i in range(1, n + 1):
    print(i, size)
    size *= (1 + p / 100)
    