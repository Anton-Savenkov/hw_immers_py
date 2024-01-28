"""
Улучшаемзадачу2.
Добавьте возможность запуска функции “угадайки” из
модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов:параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""

from sys import argv

from task02 import guessing_game as game

print('start')
print(argv)
print('stop')

# min, max, triers = map(int, argv[1:])
args = [int(el) for el in argv[1:]]

game(args[0], args[1], args[2])