a, b, c, d = 28, 30, 31, 365

for n in range(1, d // a):
    for k in range(1, d // b):
        for m in range(1, d // c):
            if a * n + b * k + c * m == d:
                print(f'n = {n}, k = {k}, m = {m}')