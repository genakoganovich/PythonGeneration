a, b = map(int, [input() for _ in range(2)])

max_i = a
max_sum = 0

for i in range(a, b + 1):
    i_sum = sum(filter(lambda x: not i % x, list(range(1, i + 1))))
    if i_sum >= max_sum:
        max_i = i
        max_sum = i_sum
print(max_i, max_sum)
