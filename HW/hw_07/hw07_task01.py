"""
Напишите функцию группового переименования файлов в папке
test_folder под названием rename_files. Она должна:

a. принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории
"""


import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)


# Заполнить тестовую папку
for i in range(10):

    file_name = f"test{i}.txt"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()

file_name = "test.doc"
file_path = os.path.join(folder_path, file_name)

with open(file_path, "w") as file:
    file.write("This is a test file.\n")
    file.close()





import warnings

warnings.filterwarnings('ignore')

# Введите ваше решение ниже - верное решение <-->

import os
import glob

__all__ = ['rename_files']

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=None):
    folder_path = "test_folder"
    files = glob.glob(os.path.join(folder_path, f'*.{source_ext}'))

    if not name_range:
        name_range = [0, len(desired_name)]

    for i, file_path in enumerate(files, start=1):
        file_name = os.path.basename(file_path)
        original_name = file_name[: file_name.rindex('.')]
        original_name = original_name[name_range[0]:name_range[1]]

        new_name = f"{desired_name}{str(i).zfill(num_digits)}.{target_ext}"
        os.rename(file_path, os.path.join(folder_path, new_name))

# <<<--->>>




#При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

#При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки

# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")


rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

folder_content = ""
files = os.listdir(folder_path)
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)