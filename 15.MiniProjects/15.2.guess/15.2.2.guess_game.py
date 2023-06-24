import random

results = {'start': 'Добро пожаловать в числовую угадайку',
           'prompt': 'Введите целое число от 1 до 100',
           'prompt2': 'А может быть все-таки введем целое число от 1 до 100?',
           'smaller': 'Ваше число меньше загаданного, попробуйте еще разок',
           'bigger': 'Ваше число больше загаданного, попробуйте еще разок',
           'winner': 'Вы угадали, поздравляем!',
           'end': 'Спасибо, что играли в числовую угадайку. Еще увидимся...'}


def is_valid(s):
    return str(s).isdigit() and int(s) in range(1, 101)


def make_sure_valid(s):
    while not is_valid(s):
        print(results['prompt2'])
        s = input()
    return s


def get_guess(s):
    return int(make_sure_valid(s))


def play(num, count, win):
    while not win:
        count += 1
        guess = get_guess(input())
        if guess < num:
            print(results['smaller'])
        elif guess > num:
            print(results['bigger'])
        else:
            win = True
            print(results['winner'])
            print(f'Число попыток = {count}')


def prompt_continue():
    again = input('Сыграть новую игру? (д = да, н = нет): ')
    return True if again.lower() == 'д' else False


def run():
    print(results['start'])
    is_ready = True
    while is_ready:
        print(results['prompt'])
        play(random.randint(1, 100), 0, False)
        is_ready = prompt_continue()
    print(results['end'])
