def get_factors(num):
    return list(filter(lambda x: not num % x, range(1, num + 1)))


# объявление функции
def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
