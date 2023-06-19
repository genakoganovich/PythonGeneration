n = int(input())

a = 0
b = 1

for i in range(1, n + 1):
    for j in range(a + b, i + a + b):
        print(j, end=' ')
    print()
    a, b = i, a + b
