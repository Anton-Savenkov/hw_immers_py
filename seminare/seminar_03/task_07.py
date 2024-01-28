"""
Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
"""

# решение 1 с использованием метода count
data = input("Введите строку текста: ")
dct = {}
for el in data:
    val = data.count(el)
    dct[el] = val
print(dct)

# решение 1 без использования метода count
data = input("Введите строку текста: ")
dct = {}
for el_1 in data:
    count = 0
    for el_2 in data:
        if el_1 == el_2:
            count += 1

    dct[el_1] = count
print(dct)

# решение 2 без использования метода count
string = input('Введите строку: ')
my_dict = {}
for char in string:
    if char.isalpha():
        my_dict[char] = my_dict.get(char, 0) + 1
print(my_dict)

# решение 2 с использованием метода count
for char in string:
    if char.isalpha():
        my_dict[char] = string.count(char)
print(my_dict)

"""
data = 'dasdasd asdasdas dasddsa adasdads addad'
my_dict = {}
for el in data:
    if el.isalpha():
        my_dict[el] = data.count(el)
print(my_dict)

my_dict = {el: data.count(el) for el in data if el.isalpha()}
print(my_dict)

my_dict = {}
for el_1 in data:
    if el_1.isalpha():
        count = 0
        for el_2 in data:
            if el_1 == el_2:
                count += 1
        my_dict[el_1] = count

print(my_dict)

my_dict = {}
for el in data:
    if el.isalpha():
        my_dict[el] = my_dict.get(el, 0) + 1
print(my_dict)
"""