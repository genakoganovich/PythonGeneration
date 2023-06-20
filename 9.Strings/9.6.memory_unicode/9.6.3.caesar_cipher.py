# n = int(input())
# s = input()
#
# list(map(lambda x: print(chr(ord(x) - n), end=''), s))

s = 'fsfftsfufksttskskt'
t = 'rerrfergrweffewewf'


list(map(lambda i: print(str(ord(t[i])), end=' '), range(len(s))))
print()

list(map(lambda i: print(str(ord(s[i])), end=' '), range(len(s))))
print()


list(map(lambda i: print(str(ord(t[i]) - ord(s[i])), end=' '), range(len(s))))
