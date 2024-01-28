"""
 Задание No1
✔ Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

"""

def my_func(text):
    text_lst = []
    count = 1
    for el in text.split():
        text_lst.append(f'{count} {el}')
        count += 1
    result_text = ".\n" .join('{}'.format(el) for el in text_lst)

    return result_text



print(my_func('Hello world, go action'))
text = 'Hello world go action'

