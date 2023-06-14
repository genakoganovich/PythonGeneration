value = int(input())


def is_in_range(v, a, b):
    return a < v < b


print('Принадлежит' if is_in_range(value, -30, -1) or is_in_range(value, 7, 26) else 'Не принадлежит')
