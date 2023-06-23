numbers = list(map(int, input().split()))

min_value = min(numbers)
index_min = numbers.index(min_value)
max_value = max(numbers)
index_max = numbers.index(max_value)

numbers[index_min] = max_value
numbers[index_max] = min_value

print(*numbers)
