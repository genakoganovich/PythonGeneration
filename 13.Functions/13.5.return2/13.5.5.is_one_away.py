def count_difference(word1, word2):
    return sum([word1[i] != word2[i] for i in range(len(word1))])


# объявление функции
def is_one_away(word1, word2):
    return len(word1) == len(word2) and count_difference(word1, word2) == 1

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
