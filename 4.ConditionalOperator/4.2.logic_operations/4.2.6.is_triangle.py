def is_triangle(sides):
    return sides[0] < sides[1] + sides[2] and sides[1] < sides[0] + sides[2] and sides[2] < sides[0] + sides[1]


print('YES' if is_triangle(list(map(int, [input() for _ in range(3)]))) else 'NO')
