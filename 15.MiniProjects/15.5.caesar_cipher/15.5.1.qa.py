ru = ['а', 32]
en = ['a', 26]
punctuation = ' .,;:!?'


def encrypt_c(c, k, first, length):
    return chr((ord(c) - ord(first) + k) % length + ord(first))


def encrypt(string, k, first, length):
    result = []
    for c in string:
        if c in punctuation:
            c_new = c
        else:
            c_new = encrypt_c(c.lower(), k, first, length)
            if str(c).isupper():
                c_new = c_new.upper()
        result.append(c_new)
    return ''.join(result)


def encrypt_en(string, k):
    result = []
    for c in string:
        if not str(c).isascii():
            c_new = c
        else:
            c_new = encrypt_c(c.lower(), k, 'a', 26)
            if str(c).isupper():
                c_new = c_new.upper()
        result.append(c_new)
    return ''.join(result)


