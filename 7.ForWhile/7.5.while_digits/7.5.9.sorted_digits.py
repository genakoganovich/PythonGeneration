digits = list(map(int, input()))

print('YES' if digits == sorted(digits, reverse=True) else 'NO')
