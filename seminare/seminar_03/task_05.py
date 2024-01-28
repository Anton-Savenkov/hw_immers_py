"""
Задание №5
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
"""

# традиционный итератор с функцией append
lst = [2, 2, 2, 3, 3, 5]
lst_numbers = []
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        lst_numbers.append(i + 1)
print(lst_numbers)

# list comprehension
lst_numbers = [i + 1 for i in range(len(lst)) if lst[i] % 2 == 1]
print(lst_numbers)

"""
lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
res = []

for i in range(len(lst)):
    if lst[i] % 2 == 1:
        res.append(i + 1)

print(res)

res2 = [i + 1 for i in range(len(lst)) if lst[i] % 2 == 1]

print(res2)
"""