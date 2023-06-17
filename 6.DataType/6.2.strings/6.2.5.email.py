week_end = ['@', '.']
email = input()
print('YES' if all([x in email for x in week_end]) else 'NO')
