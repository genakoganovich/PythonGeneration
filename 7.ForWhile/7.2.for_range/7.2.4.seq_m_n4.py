m, n = map(int, [input() for _ in range(2)])


for i in range(m, n + 1):
    if not i % 17 or not i % 3 and not i % 5 or i % 10 == 9:
        print(i)
