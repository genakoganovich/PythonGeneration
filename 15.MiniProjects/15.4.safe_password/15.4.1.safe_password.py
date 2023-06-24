import random


def get_answer(prompt):
    answer = input(prompt)
    return True if answer.lower() == 'д' else False


def generate_password(length, letters):
    result = ''
    for _ in range(length):
        result += random.choice(letters)
    return result


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous = 'il1Lo0O'

chars = ''

char_info = [[digits, f'Включать ли цифры {digits}: '],
             [lowercase_letters, f'Включать ли строчные буквы {lowercase_letters}: '],
             [uppercase_letters, f'Включать ли прописные буквы {uppercase_letters}: '],
             [punctuation, f'Включать ли символы {punctuation}: '],
             [ambiguous, f'Исключать ли неоднозначные символы {ambiguous}: ']
             ]


n = int(input('Количество паролей для генерации: '))
pass_length = int(input('Длина одного пароля: '))

for row in char_info:
    if get_answer(row[1]):
        chars += row[0]


print(*[generate_password(pass_length, chars) for _ in range(n)], sep='\n')

