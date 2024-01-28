"""
📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл
в формате CSV.
"""

import json
import os


def update_user_data():
    user_data = {}  # Создаем словарь для хранения данных
    json_file = 'user_data.json'

    if os.path.exists(json_file):  # Если файл существует, загружаем данные
        with open(json_file, 'r') as file:
            user_data = json.load(file)

    while True:
        name = input("Введите имя пользователя (или 'exit' для выхода): ")
        if name.lower() == 'exit':
            break
        identifier = input("Введите личный идентификатор: ")
        access_level = int(input("Введите уровень доступа (от 1 до 7): "))

        # Проверка, чтобы идентификатор пользователя был уникальным независимо от уровня доступа
        while identifier in user_data:
            print(
                "Пользователь с таким идентификатором уже существует. Пожалуйста, введите другой идентификатор.")
            identifier = input("Введите личный идентификатор: ")

        # Обновляем информацию о пользователе в словаре
        user = {'name': name, 'access_level': access_level}
        user_data[identifier] = user

        # Группируем пользователей по уровню доступа
        grouped_data = {level: {key: user_data[key] for key in user_data if
                                user_data[key]['access_level'] == level} for
                        level in range(1, 8)}

        # Записываем обновленные данные в json файл
        with open(json_file, 'w') as file:
            json.dump(grouped_data, file, indent=4)

    print("Данные успешно обновлены и сохранены в файле 'user_data.json'")

update_user_data()