def is_prime(num):
    return not any(not num % n for n in range(2, num)) and num > 1


# объявление функции
def get_next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
