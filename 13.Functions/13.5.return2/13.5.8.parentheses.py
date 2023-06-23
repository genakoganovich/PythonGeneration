# объявление функции
LEFT = '('
RIGHT = ')'


def is_correct_bracket(text):
    stack = list()
    for c in text:
        if not stack or c == LEFT or c == RIGHT and stack[-1] == RIGHT:
            stack.append(c)
        else:
            stack.pop()
    return not stack


# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))