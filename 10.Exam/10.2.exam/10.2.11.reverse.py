def reverse(s):
    return s[::-1]


s = input()
first = s.find('h')
last = s.rfind('h')


print(s[:first + 1] + reverse(s[first + 1:last]) + s[last:])
