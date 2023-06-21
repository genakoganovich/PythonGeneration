numbers = [8, 9, 10, 11]

numbers.pop(1)
numbers.insert(1, 17)

for n in range(4, 7):
    numbers.append(n)

numbers.pop(0)

numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)
