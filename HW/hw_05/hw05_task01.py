"""
Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

"""
"""
эталонное решение 
def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)
"""

file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    path = file_path[:file_path.rindex('/')]
    file_name_with_extension = file_path[file_path.rindex('/') + 1:]
    file_name = file_name_with_extension[:file_name_with_extension.rindex('.')]
    file_extension = file_name_with_extension[file_name_with_extension.rindex('.'):]
    return path, file_name, file_extension

# Пример использования функции
#file_path = "/home/user/documents/example.txt"
info = get_file_info(file_path)
print(info)  # Вывод: ('/home/user/documents', 'example', '.txt')