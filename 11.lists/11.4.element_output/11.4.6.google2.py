strings = [input() for _ in range(int(input()))]
queries = [input() for _ in range(int(input()))]

print(*list(filter(lambda x: all(q.lower() in str(x).lower() for q in queries), strings)), sep='\n')
