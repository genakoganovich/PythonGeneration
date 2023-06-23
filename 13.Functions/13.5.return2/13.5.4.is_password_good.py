# объявление функции
def is_password_good(password):
    return len(password) > 7 \
        and any(str(c).isupper() for c in password) \
        and any(str(c).islower() for c in password) \
        and any(str(c).isdigit() for c in password)


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
