def format_number(num):
    return num if num % 1 else int(num)


def get_human_age(dog_age):
    return dog_age * 10.5 if dog_age < 3 else 2 * 10.5 + (dog_age - 2) * 4


def run(dog_age):
    print(format_number(get_human_age(dog_age)))


run(int(input()))
