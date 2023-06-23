import numpy as np

numbers = np.array(list(map(int, [input() for _ in range(int(input()))])))
print(*numbers, sep='\n')
print()
print(*(numbers ** 2 + 2 * numbers + 1), sep='\n')
