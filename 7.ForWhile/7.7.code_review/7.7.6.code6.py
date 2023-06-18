n = int(input())  # n = input()
product = 1  # product = n % 10
while n > 0:  # while n >= 10:
    digit = n % 10
    product = product * digit
    n //= 10
print(product)