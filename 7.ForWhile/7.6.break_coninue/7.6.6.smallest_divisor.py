n = int(input())

for i in range(2, n + 1):
    if not n % i:
        print(i)
        break
