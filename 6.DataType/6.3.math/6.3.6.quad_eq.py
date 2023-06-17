import math


def solve_quad_eq(a, b, c):
    d = b ** 2 - 4 * a * c
    return ['Нет корней'] if d < 0 \
        else [-b / (2 * a)] if d == 0 \
        else [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]


def run(solution):
    print(*solution if len(solution) == 1 else '\n'.join([min(solution), max(solution)]))


run(solve_quad_eq(*map(float, [input() for _ in range(3)])))
