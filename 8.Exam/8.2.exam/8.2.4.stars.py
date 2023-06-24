n = int(input())

print('*' * 19)
space = ' ' * 17
for _ in range(1, n - 1):
    print(space.join(['*', '*']))
print('*' * 19)
