s = input()
count = s.count('f')


if count == 0:
    print('NO')
elif count == 1:
    print(s.index('f'))
else:
    print(s.index('f'), s.rindex('f'))
