import numpy as np

arr = np.array(list(map(int, [input() for _ in range(10)])))
print(np.prod(arr[arr != 0]))
