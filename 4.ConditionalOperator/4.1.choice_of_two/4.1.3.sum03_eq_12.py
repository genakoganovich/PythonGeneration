value = input()
print('ДА' if int(value[0]) + int(value[-1]) == int(value[1]) - int(value[2]) else 'НЕТ')
