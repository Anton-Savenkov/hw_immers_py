"""
Задание №5
Работа в консоли в режиме интерпретатора Python.
Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""

n = int(input("задайте n: "))
e = int(input("задайте n: "))

sum_num = 0
el = 0

while el <= n:
    el += 1
    if el % 2 == 0:
        if el % e == 0:
            continue
        sum_num += el
print(sum_num)

while el <= n:
    if el % 2  == 0 and el % 3 == 0:
        sum_num += el
print(sum_num)