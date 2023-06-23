import numpy as np

numbers = np.array([int(input()) for _ in range(int(input()))])

print(*numbers[numbers < 0], sep='\n')
print(*numbers[numbers == 0], sep='\n')
print(*numbers[numbers > 0], sep='\n')
