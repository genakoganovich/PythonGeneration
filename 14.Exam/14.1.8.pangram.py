import string

# объявление функции
def is_pangram(text):
    return all(c in text.lower() for c in string.ascii_lowercase)


# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
