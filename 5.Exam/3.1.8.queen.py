x1, y1, x2, y2 = map(int, [input() for _ in range(4)])


print('YES' if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2 else 'NO')
