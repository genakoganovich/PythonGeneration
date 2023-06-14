squares = [input() for _ in range(4)]
print('YES' if any([squares[0] == squares[2], squares[1] == squares[3]]) else 'NO')
