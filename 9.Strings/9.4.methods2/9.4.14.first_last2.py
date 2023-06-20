c, s = 'f', input()
b, e = s.find(c), s.rfind(c)
print('NO' if b < 0 else b, str(e) * (e > b))
