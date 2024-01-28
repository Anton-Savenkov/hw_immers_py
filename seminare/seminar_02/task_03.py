"""
Задание №3
✔ Напишите программу, которая получает целое число и возвращает
его двоичное, восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего
результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода
в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно
"""

number = 125
base = 2
res = ''
while number > 0:
    res = str(number % base) + res
    number //= base
print(res)

number = 125
print(bin(number))

number = 125
base = 8
res = ''
while number > 0:
    res = str(number % base) + res
    number //= base
print(res)

number = 125
print(oct(number))

number = 125
base = 16
res = ''
while number > 0:
    res = str(number % base) + res
    number //= base
print(res)

number = 125
print(hex(number))
