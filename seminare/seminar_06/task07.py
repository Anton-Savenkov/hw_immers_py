"""
Создайте модуль и напишите в нём функцию,которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину,если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся,что год может быть в диапазоне [1, 9999].
Весь период (1января 1года-31декабря 9999года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""

def func(date):

    day, month, year = map(int, date.split('.'))
    if year in range(1000, 2024) and month in range(1, 13) and day in range(1, 32):
        if year % 400 == 0 and month == 2 or year % 4 == 0 and year % 100 != 0 and month == 2:
            if day in range(1, 30):
                return True
            else:
                return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return True
        elif month == 2:
            if day in range(1, 29):
                return True
            else:
                return False
        else:
            if day in range(1, 31):
                return True
            else:
                return False
    else:
        return False


print(func('12.02.2009'))