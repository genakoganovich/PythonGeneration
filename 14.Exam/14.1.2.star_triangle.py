# объявление функции
def draw_triangle():
    base = 15
    h = 8
    for i in range(0, h):
        print(' ' * (base // 2 - i) + '*' * (2 * i + 1))


# основная программа
draw_triangle()  # вызов функции
