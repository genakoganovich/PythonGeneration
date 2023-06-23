numbers = list(map(int, [input() for _ in range(int(input()))]))
result = [numbers[i] + numbers[i + 1] for i in range(len(numbers) - 1)]
print(result)
