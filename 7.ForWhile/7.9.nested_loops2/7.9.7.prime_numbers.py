a, b = map(int, [input() for _ in range(2)])

for i in range(a, b + 1):
    if not len(list(filter(lambda x: not i % x, range(2, i)))) and i != 1:
        print(i)
