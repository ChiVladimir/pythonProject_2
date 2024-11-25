# Домашнее задание по теме "Генераторы"
import itertools

def all_variants(text):

    for i in range(1, len(text)+1):
        comb_ = list(itertools.combinations(text, i))
        for j in range(0, len(comb_)):
            yield ''.join(comb_[j])



a = all_variants("abc")
for i in a:
    print(i)


