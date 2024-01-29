"""
На вход подается словарь со списком вещей для похода
в качестве ключа и их массой max_weight в качестве значения.

Определите какие вещи влезут в рюкзак backpack передав его
максимальную грузоподъёмность.
Результат должен быть в виде словаря {предмет:вес}
с вещами в рюкзаке и сохранен в переменную backpack.

Достаточно получить один допустимый вариант и сохранить в
переменную backpack. Не выводите backpack на экран.
"""

#решение проверено, ок
items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

backpack = {}
for k, v in items.items():
    if max_weight - v >= 0:
        backpack[k] = v
        max_weight = max_weight - v

print(backpack)

"""
# первое решение с функией
def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

items = {'tent': 5, 'water': 3, 'food': 4, 'clothes': 2, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight))
"""