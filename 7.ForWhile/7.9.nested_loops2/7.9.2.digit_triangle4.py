n = int(input())

for i in range(n):
    for j in range((2 * i + 1) // 2 + 1):
        print(j + 1, end='')

    for j in range((2 * i) // 2 + 1, 1, -1):
        print(j - 1, end='')
    print()
