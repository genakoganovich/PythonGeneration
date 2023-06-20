s = input()

print(sum(map(lambda i: s[i] == s[i + 1], range(len(s) - 1))))
