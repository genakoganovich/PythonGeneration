n = int(input())

a = b = 1

if n == 1:
    print(a, end=' ')

if n > 1:
    print(a, b, end=' ')

for i in range(2, n):
    a, b = b, a + b
    print(b, end=' ')
