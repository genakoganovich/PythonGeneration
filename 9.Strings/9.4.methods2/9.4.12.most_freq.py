s = input()
counts = [s.count(x) for x in s]
print(s[len(s) - 1 - counts[::-1].index(max(counts))])
