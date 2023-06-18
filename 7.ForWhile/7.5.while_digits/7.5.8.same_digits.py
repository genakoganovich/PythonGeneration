import numpy as np

digits = np.array(list(map(int, input())))
print('YES' if np.all(digits == [digits[0]]) else 'NO')
