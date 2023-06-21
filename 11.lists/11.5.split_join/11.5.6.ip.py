print('ДА' if all(0 <= int(n) <= 255 for n in input().split('.')) else 'НЕТ')
