n = int(input())

numbers = list(map(int, [input() for _ in range(n)]))
largest_number = max(numbers)
print(largest_number)
numbers.remove(largest_number)
print(max(numbers))
