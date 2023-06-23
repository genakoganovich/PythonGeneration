import calendar


# объявление функции
def get_days(month):
    return calendar.monthrange(2019, month)[1]


# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
