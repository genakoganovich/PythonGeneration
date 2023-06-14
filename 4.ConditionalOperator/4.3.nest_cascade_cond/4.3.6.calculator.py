import operator

ops = {"+": operator.add, "-": operator.sub, '*': operator.mul, '/': operator.truediv}
a, b = map(int, [input() for _ in range(2)])
op = input()

print('Неверная операция' if op not in ops else 'На ноль делить нельзя!' if op == '/' and b == 0 else ops[op](a, b))
