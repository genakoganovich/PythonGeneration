m, n = map(int, [input() for _ in range(2)])


for i in range(m + m % 2 - 1, n - 1, -2):
    print(i)
