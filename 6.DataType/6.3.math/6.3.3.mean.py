import math

a, b = map(float, [input() for _ in range(2)])

print((a + b) / 2)
print(math.sqrt(a * b))
print(2 * a * b / (a + b))
print(math.sqrt((a ** 2 + b ** 2) / 2))
