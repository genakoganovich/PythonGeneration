# объявление функции
def is_prime(num):
    return not any(not num % n for n in range(2, num)) and num > 1


def is_palindrome(text):
    return text == text[::-1]


def is_even(num):
    return not num % 2


def has_valid_details(details):
    if len(details) != 3:
        return False
    return is_palindrome(details[0]) \
        and is_prime(int(details[1])) and is_even(int(details[2]))


def is_valid_password(password):
    return has_valid_details(password.split(':'))


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
