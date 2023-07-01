import re

s = input()
print('YES' if re.match(r'\d{3}-\d{3}-\d{4}', s) or re.match(r'7-\d{3}-\d{3}-\d{4}', s) else 'NO')
