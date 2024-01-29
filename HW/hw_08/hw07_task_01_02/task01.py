"""
Ваша задача - написать программу, которая принимает на вход директорию
и рекурсивно обходит эту директорию и все вложенные директории.
Результаты обхода должны быть сохранены в нескольких форматах:
JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

Путь к файлу или директории: Абсолютный путь к файлу или директории.
Тип объекта: Это файл или директория. Размер: Для файлов - размер в байтах,
для директорий - размер, учитывая все вложенные файлы и директории в байтах.

Важные детали:
Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

Для файлов сохраните их размер в байтах.

Для директорий, помимо их размера, учтите размер всех файлов и директорий,
находящихся внутри данной директории, и вложенных директорий.

Программа должна использовать рекурсивный обход директорий, чтобы учесть все
вложенные объекты.

Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle.
Форматы файлов должны быть выбираемыми.

Для обхода файловой системы вы можете использовать модуль os.

Вам необходимо написать функцию traverse_directory(directory),
которая будет выполнять обход директории и возвращать результаты
в виде списка словарей. После этого результаты должны быть сохранены
в трех различных файлах (JSON, CSV и Pickle)
с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
"""

#print(os.path.abspath(__file__))
#print("File Path:", Path(__file__).absolute())
#print("Directory Path:", Path().absolute())


import os
import json
import csv
import pickle

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_directory_size(dp)  # Рекурсивно вызываем эту же функцию для каждой поддиректории
    return total_size


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            results.append ({'Path': file_path, 'Type': 'File',
                             'Size': file_size})

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            results.append ({'Path': dir_path, 'Type': 'Directory',
                             'Size': dir_size})

    return results

def save_results_to_json(results, output_file):
    with open(output_file, 'w') as file:
        json.dump(results, file, indent=4)

def save_results_to_csv(results, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        writer.writerows(results)

def save_results_to_pickle(results, output_file):
    with open(output_file, 'wb') as file:
        pickle.dump(results, file)

# Пример исполнения
directory = '/Users/asave/DOK_i/Education/GB/II_year/immersion_in_Python/immers_py/HW/hw_08/'
directory_results = traverse_directory(directory)

save_results_to_json(directory_results, 'directory_results.json')
save_results_to_csv(directory_results, 'directory_results.csv')
save_results_to_pickle(directory_results, 'directory_results.pickle')
