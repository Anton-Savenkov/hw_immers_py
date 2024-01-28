"""
В большой текстовой строке text подсчитать количество встречаемых слов и
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд
(после того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.
"""
import re
from collections import Counter

text = "Python 3.9 is the latest version of Python. It's awesome!"
#приводим текст к нижнему регистру
#избавляемся от знаков припинания
#разбиваем текст на элементы через пробел
text = re.sub(r'[^\w\s]', ' ', text.lower()).split()
# второой варинт удаления знаков припинания (import string)
# text = text.translate(str.maketrans('','', string.punctuation))

# Считаем количество повторяющихся слов
word_counts = Counter(text)
# Исключаем слова, состоящие только из цифр
word_counts = {word: count for word, count in word_counts.items() if not word.isdigit()}
# Сортируем слова по убыванию количества повторений
common_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# Возвращаем 10 самых часто встречающихся слов
res = common_words[:10]
print(res)


"""
эталонное решение
"""
import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)
