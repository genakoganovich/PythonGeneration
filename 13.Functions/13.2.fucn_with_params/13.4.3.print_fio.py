# объявление функции
def print_fio(name, surname, patronymic):
    print(*map(lambda x: str(x).upper(), [surname[0], name[0], patronymic[0]]), sep='')


# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)
