"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""
from math import pi

d = 100
l = d * pi
s = pi * (d / 2) ** 2
print(f'{l:.42f}, {s:.42f}')