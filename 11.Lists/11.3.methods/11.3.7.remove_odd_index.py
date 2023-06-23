numbers = list(map(int, [input() for _ in range(int(input()))]))
del numbers[1::2]
print(numbers)
