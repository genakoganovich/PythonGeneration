s = input()
print(f"{s.replace(' ', '+')}={sum(list(map(int, s.split())))}")
