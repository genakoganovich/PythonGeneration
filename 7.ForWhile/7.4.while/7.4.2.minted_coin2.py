n = int(input())
total = n // 25 + (n % 25) // 10 + ((n % 25) % 10) // 5 + (((n % 25) % 10) % 5)
print(total)
