# Произвольное число параметров

def single_root_words(root_word, *other_words):
    list_of_results = list()
    i = 0
    for i in range(len(other_words)):
        a = root_word.lower()
        b = other_words[i].lower()
        if a in b or b in a:
            list_of_results.append (other_words[i])
    i += 1
    return list_of_results


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
