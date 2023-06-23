strings = [input() for _ in range(int(input()))]
query = input()

print(*list(filter(lambda x: query.lower() in str(x).lower(), strings)), sep='\n')
