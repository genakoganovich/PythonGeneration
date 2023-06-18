n = int(input())

print(sum([m for m in range(1, n + 1) if not n % m]))
