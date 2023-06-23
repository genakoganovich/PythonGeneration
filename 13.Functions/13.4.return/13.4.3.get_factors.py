# объявление функции
def get_factors(num):
    return list(filter(lambda x: not num % x, range(1, num + 1)))

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
