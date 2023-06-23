import re


# объявление функции
def convert_to_python_case(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
