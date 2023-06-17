age, sex = [input() for _ in range(2)]

print('YES' if sex == 'f' and 10 <= int(age) <= 15 else 'NO')
