def get_dist(x, y):
    return abs(x - y)


def is_in_radius(squares, r=1):
    return all([get_dist(squares[0], squares[2]) <= r, get_dist(squares[1], squares[3]) <= r])


print('YES' if is_in_radius(list(map(int, [input() for _ in range(4)]))) else 'NO')
