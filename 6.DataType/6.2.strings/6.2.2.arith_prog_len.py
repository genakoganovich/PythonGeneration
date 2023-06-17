cities = sorted([input() for _ in range(3)], key=lambda x: len(x))
print('YES' if len(cities[1]) + len(cities[1]) - len(cities[0]) == len(cities[2]) else 'NO')
