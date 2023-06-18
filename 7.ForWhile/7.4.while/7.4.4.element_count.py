the_end = ['стоп', 'хватит', 'достаточно']

count = 0
string = input()
while string.lower() not in the_end:
    count += 1
    string = input()

print(count)
