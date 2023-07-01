import math


# объявление функции
def compute_binom(n, k):
    return int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))


# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))
