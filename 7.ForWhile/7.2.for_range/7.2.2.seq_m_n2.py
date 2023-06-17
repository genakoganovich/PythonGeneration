m, n = map(int, [input() for _ in range(2)])

step = 1 if m < n else -1
for i in range(m, n + step, step):
    print(i)
