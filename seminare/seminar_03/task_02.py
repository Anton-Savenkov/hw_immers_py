"""
Задание №2
Погружение в Python | Коллекции
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

lst = [1, 2.1, True, -5, "Sds"]
for el in lst:
    try:
        print(int(el))
        print(float(el))
        if type(el) == str and not el.islower():
            print(el.lower())
    except ValueError:
        print(f"Невозможно преобразовать {el} к целому положительному числу")
        print(f"Невозможно преобразовать {el} к вещественному числу")
    except TypeError:
        print("Ошибка")



"""

data = input('Введите данные: ')

if data.isdigit():
    print(int(data))
elif data.find('.') and data.replace('.', '').isdigit():
    print(float(data))
elif any([el.isupper() for el in data]):
    print(data.lower())
else:
    print(data)
    
"""