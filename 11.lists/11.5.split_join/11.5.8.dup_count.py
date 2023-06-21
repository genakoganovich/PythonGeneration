numbers = list(map(int, input().split()))


count = 0
for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
print(count)
