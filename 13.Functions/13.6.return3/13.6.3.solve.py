import math


# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    return sorted([(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)])


# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)