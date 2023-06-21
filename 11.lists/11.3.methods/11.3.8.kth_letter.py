strings = [input() for _ in range(int(input()))]
k = int(input()) - 1

strings = list(filter(lambda x: len(x) > k, strings))
list(map(lambda x: print(x[k], end=''), strings))
