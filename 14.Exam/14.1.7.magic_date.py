# объявление функции
def is_magic(date):
    date_num = list(map(int, date.split('.')))
    return date_num[0] * date_num[1] == date_num[2] % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))
