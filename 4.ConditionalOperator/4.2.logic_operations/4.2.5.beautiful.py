def is_beautiful(input_value):
    value = int(input_value)
    return len(input_value) == 4 and not (value % 7 and value % 17)


print('YES' if is_beautiful(input()) else 'NO')
