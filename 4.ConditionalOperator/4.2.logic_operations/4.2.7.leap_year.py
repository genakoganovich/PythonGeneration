def is_leap(year):
    return not year % 4 and year % 100 or not year % 400


print('YES' if is_leap(int(input())) else 'NO')
