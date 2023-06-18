n = int(input())

count = 0
while n in range(0, 6):
    if n == 5:
        count += 1
    n = int(input())

print(count)
