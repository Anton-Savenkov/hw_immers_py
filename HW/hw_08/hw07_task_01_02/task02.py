"""
Из созданных на уроке и в рамках домашнего задания функций,
соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory.
"""

code_to_write = '''
import os
import json
import csv
import pickle

__all__ = ['get_dir_size', 'traverse_directory', 
           'save_results_to_json', 'save_results_to_csv', 
           'save_results_to_pickle']

def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
        for d in dirnames:
            dp = os.path.join(dirpath, d)
            total_size += get_dir_size(dp)  # Рекурсивно вызываем эту же функцию для каждой поддиректории
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
            dir_size = get_dir_size(dir_path)
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
'''

with open("__init__.py", "w") as init_file:
    init_file.write(code_to_write)