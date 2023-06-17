week_end = ['суббота', 'воскресенье']
string = input()
print('YES' if any([x in string for x in week_end]) else 'NO')
