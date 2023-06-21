n = int(input())

print(list(filter(lambda i: not n % i, list(range(1, n + 1)))))
