def mult_gt7(string):
    result = 1
    for x in string:
        if int(x) > 7:
            result *= int(x)
    return result


s = input()

print(len(list(filter(lambda x: x == '3', s))))
print(s.count(s[-1]))
print(len(list(filter(lambda x: not int(x) % 2, s))))
print(sum([int(x) for x in s if int(x) > 5]))
print(mult_gt7(s))
print(sum([1 for x in s if x == '0' or x == '5']))
