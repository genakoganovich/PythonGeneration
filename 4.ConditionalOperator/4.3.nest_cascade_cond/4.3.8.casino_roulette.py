
def get_color(value, limits, colors):
    if value == 0:
        return colors[str(value)]

    for i in range(len(limits) - 1):
        r = range(limits[i], limits[i + 1])
        if value in r:
            return colors[get_key(value, r)]

    return 'ошибка ввода'


def get_key(value, r):
    return ' '.join([str(r[0]), str(r[-1]), str(bool(value % 2))])


def run():
    limits = [1, 11, 19, 29, 37]
    colors = {'0': 'зеленый',
              '1 10 True': 'красный',
              '1 10 False': 'черный',
              '11 18 True': 'черный',
              '11 18 False': 'красный',
              '19 28 True': 'красный',
              '19 28 False': 'черный',
              '29 36 True': 'черный',
              '29 36 False': 'красный'
              }

    print(get_color(int(input()), limits, colors))


run()
