"""
Создайте функцию generate_csv_file(file_name, rows), которая будет
генерировать по три случайны числа в каждой строке, от 100-1000 строк,
и записывать их в CSV-файл. Функция принимает два аргумента:

file_name (строка) - имя файла, в который будут записаны данные.
rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного
уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
None, если уравнение не имеет корней (дискриминант отрицателен).
Одно число, если уравнение имеет один корень (дискриминант равен нулю).
Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать
функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции,
исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с
помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json.
Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots
в файле results.json будет сохранена информация о параметрах и результатах
вычислений для каждой строки данных из CSV-файла.

"""

import csv
import random
import math
import json
from functools import wraps

def generate_csv_file(file_name, rows):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['Number1', 'Number2', 'Number3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(rows):
            writer.writerow({'Number1': random.randint(100, 1000),
                             'Number2': random.randint(100, 1000),
                             'Number3': random.randint(100, 1000)})


def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2


def save_to_json(func):
    @wraps(func)
    def wrapper(file_name, *args, **kwargs):
        roots_data = []
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                a, b, c = int(row['Number1']), int(row['Number2']), int(
                    row['Number3'])
                roots = func(a, b, c)
                roots_data.append({'a': a, 'b': b, 'c': c, 'roots': roots})

        with open('results.json', 'w') as jsonfile:
            json.dump(roots_data, jsonfile, indent=4)

    return wrapper

@save_to_json
def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -b / (2*a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

file_name = 'test.csv'
generate_csv_file(file_name, 100)  # Генерация CSV-файла
find_roots(file_name)  # Декорированный вызов функции find_roots, результаты сохраняются в results.json
"""
#ниже проверка  от GB
generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data)==101)

"""