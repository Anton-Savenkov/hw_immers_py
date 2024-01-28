"""
Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

# мы можем выровнять строку,
# используя {переменная:>N} где N – это общая длина

# решение 1
text = "vsdsdsdsdsds dfsfdf fdfdfd fdfdfd".split()
shift = len(max(text))
for n, el in enumerate(sorted(text), 1):
    print(f"{n}. {el:>{shift}}")

print()

# решение 2
text = "vsdsdsdsdsds dfsfdf fdfdfd fdfdfd".split()
max_len = len(max(text, key=len))
sorted_words = sorted(text, key=lambda el: el.lower())
for n, el in enumerate(sorted_words, 1):
    print(f'{n}.{el.rjust(max_len + 1)}')

"""
data = 'Hellosdasd my sir'.split()
shift = len(max(data))
for i, el in enumerate(sorted(data), 1):
    print(f'{i}. {el:>{shift}}')
"""