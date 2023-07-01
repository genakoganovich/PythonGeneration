def convert(s):
    return s[1:] + s[0] + 'ки'


print(' '.join([convert(s) for s in input().split()]))
