n = 4
count = 0
maximum_init = False
maximum = 0
for _ in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if not maximum_init:
            maximum = x
            maximum_init = True
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')