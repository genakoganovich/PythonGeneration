import numpy as np

n = int(input())
print(np.sum(np.divide(np.ones(n), np.arange(1, n + 1))) - np.log(n))
