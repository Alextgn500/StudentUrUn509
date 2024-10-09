import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = [word.lower().strip(',.=!?;: -') for word in file.read().split()]
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            try:
                position = words.index(word.lower())
                result[file_name] = position + 1
            except ValueError:
                pass
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            result[file_name] = count
        return result

# Создание файла 'test_file.txt'
content = """it's a text for task
найти везде используйте его для самопроверки
успехов в решении задачи
text text text"""

with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write(content)



# Использование класса WordsFinder
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
