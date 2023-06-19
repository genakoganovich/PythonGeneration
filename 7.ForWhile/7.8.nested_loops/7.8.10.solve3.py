min_n = 1
max_n = 150
step_n = 26

for a in range(min_n, max_n, step_n):
    for b in range(min_n, max_n, step_n):
        for c in range(min_n, max_n, step_n):
            for d in range(min_n, max_n, step_n):
                for e in range(min_n, max_n, step_n):
                    if pow(a, 5) + pow(b, 5) + pow(c, 5) + pow(d, 5) == pow(e, 5):
                        print(f'a = {a}, b = {b}, c = {c}, d = {d}, e = {e} ')
