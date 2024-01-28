"""
Задание No2
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и
верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано,возвращается истина,а если попытки исчерпаны - ложь.
"""
from random import randint

def guessing_game(min_ : int, max_ : int, tries : int)-> bool:
    num = randint(min_, max_)
    print(num)
    if num == 0:
        user_num = 1
    else:
        user_num = 0
    count = 1
    while user_num != num:
        if count > tries:
            print('Попытки закончились')
            break
        print(f'Попытка {count} из {tries}')
        user_num = int(input(f'Угадайте число из диапазона от {min_} до {max_} : '))
        if user_num > num:
            print('Заданное число меньше')
        elif user_num == num:
            print('Верно')
            return True
        else:
            print('Заданное число больше')
        count += 1
    return False

if __name__ == '__main__':
    print(guessing_game(0,2,1))