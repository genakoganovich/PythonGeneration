import numpy as np

digits = list(map(int, input()))

print(sum(digits))
print(len(digits))
print(np.prod(np.array(digits)))
print(np.mean(digits))
print(digits[0])
print(digits[0] + digits[-1])
