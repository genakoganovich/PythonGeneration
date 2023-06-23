print(*[int(x) ** 2 for x in input().split() if not int(x) % 2 and int(x) ** 2 % 10 != 4])
