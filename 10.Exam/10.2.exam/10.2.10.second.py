s = input()

count = s.count('f')
if count == 0:
    print(-2)
elif count == 1:
    print(-1)
else:
    print(s.find('f', s.find('f') + 1))
