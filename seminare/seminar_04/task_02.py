"""
 Задание No2
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.
"""

def my_func(text):
    result_lst = []
    text_lst = list(text)
    for el in text_lst:
        if el != ' ':
            result_lst.append(el.encode())

    return sorted(result_lst, reverse=True)

print(my_func('текст для проверки'))

