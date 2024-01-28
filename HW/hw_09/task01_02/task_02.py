"""
Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file.
"""
code_to_write = """
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
"""

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)