n = int(input())

for i in range(1, n + 1):
    print(i, '+'* len(list(filter(lambda x: not i % x, list(range(1, i + 1))))), sep='')
