n = 8 # n = 7
count = 0
maximum_init = False
maximum = 0 # maximum = 1000
for _ in range(1, n + 1):
    x = int(input())
    if x % 4 == 0: # if x // 4 == 0
        count += 1
        if not maximum_init:
            maximum = x
            maximum_init = True
        if x >= maximum: # if x < maximum
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')