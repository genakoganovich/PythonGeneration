import math

s = input()
lim = math.ceil(len(s) / 2)
print(s[lim:], s[:lim], sep='')
