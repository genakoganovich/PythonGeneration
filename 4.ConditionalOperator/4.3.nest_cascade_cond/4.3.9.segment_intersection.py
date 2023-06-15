a1, b1, a2, b2 = map(int, [input() for _ in range(4)])
beg = [a1, a2]
end = [b1, b2]


def get_other(this_one):
    return (this_one + 1) % 2


def get_result(this_one, other_one):
    if this_one == end.index(max(end)):
        return ' '.join(map(str, [beg[other_one], end[other_one]]))
    elif end[this_one] < beg[other_one]:
        return 'пустое множество'
    elif end[this_one] == beg[other_one]:
        return str(end[this_one])

    return ' '.join(map(str, [beg[other_one], end[this_one]]))


def run(this_one):
    print(get_result(this_one, get_other(this_one)))


run(beg.index(min(beg)))
