import math


def to_rad(deg):
    return math.pi * deg / 180


def calculate_expression(x):
    return math.sin(x) + math.cos(x) + math.tan(x) * math.tan(x)


def run(x):
    print(calculate_expression(x))


run(to_rad(float(input())))
