n = int(input())

for i in range(1, n // 2 + 1):
    for j in range(i):
        print('*', end='')
    print()

for j in range(n // 2 + 1):
    print('*', end='')
print()

for i in range(n // 2, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
