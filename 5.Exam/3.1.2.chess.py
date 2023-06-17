x1, y1, x2, y2 = map(int, [input() for _ in range(4)])


if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')