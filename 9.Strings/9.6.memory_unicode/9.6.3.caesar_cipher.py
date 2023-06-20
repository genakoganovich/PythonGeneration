n = int(input())
s = input()

list(map(lambda x: print(chr(ord('a') + (ord(x) - ord('a') + 26 - n) % 26) , end=''), s))
