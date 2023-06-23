import re


# объявление функции
def is_palindrome(text):
    text = re.sub(r'[ ,.!?-]', '', text.lower())
    return text == text[::-1]


# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
