string = input()

while len(string) > 1:
    string = str(sum(map(int, string)))
print(int(string))
