"""
Напишите программу, которая получает целое число num
и возвращает его шестнадцатеричное строковое представление.

Функцию hex используйте для проверки своего результата.
"""

num = 10
test_hex = hex(num)
base = 16
hex_list = list('0123456789abcdef')
res = ''
while num > 0:
    res = hex_list[num % base] + res
    num //= base
print(f'Шестнадцатеричное представление числа: {res.upper()}')

#num = 255
print(f'Проверка результата: {test_hex}')

"""
num = int(input('Введите число в десятичной системе: '))
print(f'Встроенная функция hex -> \t\t{hex(num)}')


def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % 16] + result
        number //= 16
    return '0x' + result


print(f'Собственная функция self_hex -> {self_hex(num)}')
"""