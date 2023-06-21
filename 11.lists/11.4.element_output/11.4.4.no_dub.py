strings = [input() for _ in range(int(input()))]
strings = sorted(set(strings), key=strings.index)
print(*strings, sep='\n')
