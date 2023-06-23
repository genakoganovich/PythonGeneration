palindromes = [n for n in range(100, 1001) if str(n) == str(n)[::-1]]

print(palindromes)
