"""
 Задание No6
📌 Напишите код, который запускается из командной строки
и получает на вход путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя логирование.

"""

import logging
import os
from collections import namedtuple
import argparse

logging.basicConfig(filename='Log/Data_log_task01.log',
                    filemode='a',
                    encoding='utf-8',
                    format='{levelname} - {asctime} : {msg}',
                    style='{',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# создание аргументов командной строки
parser = argparse.ArgumentParser(description='Принемаем заданную директорию.')
parser.add_argument('directory', type=str, help='Обработка заданного католога.')

# разбор аргументов командной строки
args = parser.parse_args()
directory_path = args.directory

# переход по указанному каталогу
data_list = [(dirs, folders, files) for dirs, folders, files in os.walk(directory_path)]

clas_list = []
Data = namedtuple('Data', ['file_name', 'file_exten', 'dir_flag', 'parent_dir'])

for i in range(0, len(data_list)):
    parent_dir = data_list[i][0]
    dir_list = data_list[i][1]
    file_list = data_list[i][2]

    for el in dir_list:
        dir_flag = 'Yes'
        file_name = el
        file_exten = ''
        d = Data(file_name, file_exten, dir_flag, parent_dir)
        clas_list.append(d)
        logger.info(f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

    for item in file_list:
        dir_flag = 'No'

        try:
            file_name, file_exten = item.split('.')
        except ValueError:
            file_name, file_exten = item, ''

        d = Data(file_name, file_exten, dir_flag, parent_dir)
        clas_list.append(d)
        logger.info(f'{file_name}, {file_exten}, {dir_flag}, {parent_dir}')

#print(*clas_list, sep="\n")