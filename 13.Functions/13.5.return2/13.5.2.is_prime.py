# объявление функции
def is_prime(num):
    return not any(not num % n for n in range(2, num)) and num > 1

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
