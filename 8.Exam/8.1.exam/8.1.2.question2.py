n = int(input())
counter = 0

for i in range(1, n + 1):
    if i % 3 == 0 and i % 7 != 0:
        counter += 1
print(counter)