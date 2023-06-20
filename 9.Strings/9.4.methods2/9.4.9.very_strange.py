n = int(input())

print(sum(map(lambda x: str(x).count('11') > 2, [input() for _ in range(n)])))
