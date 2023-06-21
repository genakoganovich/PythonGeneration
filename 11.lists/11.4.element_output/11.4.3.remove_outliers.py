numbers = list(map(int, [input() for _ in range(int(input()))]))

del numbers[numbers.index(min(numbers))]
del numbers[numbers.index(max(numbers))]

print(*numbers, sep='\n')
