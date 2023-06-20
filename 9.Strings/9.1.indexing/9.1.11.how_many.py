s = input()

list(map(lambda sym: print(f'Символ {sym} встречается {s.count(sym)} раз'), ['+', '*']))
