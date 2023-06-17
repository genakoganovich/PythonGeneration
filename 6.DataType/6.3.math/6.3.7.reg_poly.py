import math

n, a = map(float, [input() for _ in range(2)])
print(n * a ** 2 / (4 * math.tan(math.pi / n)))
