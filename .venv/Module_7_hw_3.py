# Домашнее задание по теме "Оператор "with".
# Задача "Найдёт везде"
import io
from pprint import pprint


class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_worlds = {}
        _mash = ''
        key = self.file_name
        simbols_4_delete = [',', '.', '=', '!', '?', ';', ':', ' - ']
        with open(self.file_name) as file:
            for line in file:
                for char in line.lower():
                    if char not in simbols_4_delete:
                        _mash = str(_mash) + str(char)
                    values = _mash.split()
            all_worlds = {key:values}

            return all_worlds

    def find(self, word):
        self.word = word
        found_word = {}
        key = self.file_name
        _mash = ''
        words = []
        pos = []
        with open(self.file_name) as file:
            for line in file:
                for char in line.lower():
                    _mash = str(_mash) + str(char)
                words = _mash.split()

            for i in [i for i, x in enumerate(words) if x == self.word.lower()]:
                pos.append(i + 1)
                values = pos[0]
            found_word = {key: values}
            return found_word

    def count(self, word):
        self.word = word
        found_words = {}
        key = self.file_name
        _mash = ''
        words = []
        pos = []
        with open(self.file_name) as file:
            for line in file:
                for char in line.lower():
                    _mash = str(_mash) + str(char)
                words = _mash.split()

            for i in [i for i, x in enumerate(words) if x == self.word.lower()]:
                pos.append(i + 1)
                values = len(pos)
            found_words = {key: values}

            return found_words



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder3 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder3.get_all_words())
print(finder3.find('Child'))
print(finder3.count('Child'))

finder4 = WordsFinder('Rudyard Kipling - If.txt',)
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))
