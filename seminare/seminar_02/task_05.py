"""
Задание №5
✔ Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

from math import sqrt

a = 10
b = 50
c = 100

a = b ** 2 - 4 * a * c

if d > 0:
    x_1 = (-b + sqrt(d)) / (2 * a)
    x_2 = (-b - sqrt(d)) / (2 * a)
    print(x_1, x_2)
elif d == 0:
    x = -b / (2 * a)
    print(x)
else:
    real = round(-b / (2 * a), 4)
    imaginary = round(sqrt(abs(d)) / (2 * a), 4)
    x_1 = complex(real, imaginary)
    x_2 = complex(real, -imaginary)
    print(x_1, x_2)
