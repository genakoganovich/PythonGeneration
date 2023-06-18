import numpy as np

print('YES' if np.all(np.array(list(map(int, [input() for _ in range(10)]))) % 2 == 0) else 'NO')
