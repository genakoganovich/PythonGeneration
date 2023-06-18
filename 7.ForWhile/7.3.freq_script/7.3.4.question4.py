a, b = map(int, [input() for _ in range(2)])

print(sum([1 for i in range(a, b + 1) if (i ** 3) % 10 == 4 or (i ** 3) % 10 == 9]))
