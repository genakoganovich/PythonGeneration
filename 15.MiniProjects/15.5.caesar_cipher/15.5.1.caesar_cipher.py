punctuation = ' .,;:!?"' + "'"


def count_letters(string):
    return sum([str(c).isalpha() for c in string])


def encrypt_c(c, k, first, length):
    return chr((ord(c) - ord(first) + k) % length + ord(first))


def encrypt_en(string, k):
    result = []
    for c in string:
        if c in punctuation:
            c_new = c
        else:
            c_new = encrypt_c(c.lower(), k, 'a', 26)
            if str(c).isupper():
                c_new = c_new.upper()
        result.append(c_new)
    return ''.join(result)


print(' '.join([encrypt_en(w, count_letters(w)) for w in input().split()]))