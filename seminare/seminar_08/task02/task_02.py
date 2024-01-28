"""
📌 Напишите функцию, которая в бесконечном цикле запрашивает имя,
личный идентификатор и уровень доступа (от 1 до 7).
📌 После каждого ввода добавляйте новую информацию в JSON файл.
📌 Пользователи группируются по уровню доступа.
📌 Идентификатор пользователя выступает ключём для имени.
📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
📌 При перезапуске функции уже записанные в файл данные должны сохраняться.

"""
import json
import os

def update_user_data():
    user_data = {}
    file_json = 'user_data.json'

    if os.path.exists(file_json):  # Если файл существует, загружаем данные
        with open(file_json, 'r') as file:
            user_data = json.load(file)

    while True:
        name = input('Введите имя пользователя (или "exit" для выхода): ')
        if name.lower() == "exit":
            print('Раабоота программы заавершена.')
            break
        identifier = input('Введите личный идентификатор: ')
        access_level = int(input('Ввелите уровень доступа (от 1 до 7): '))

        while identifier in user_data:
            print('Пользовааатеель с указанным идентификатором '
                  'уже существует, попробуйте другой идентификатор.')
            identifier = input('Введите личный идентификатор: ')

            user = {'name': name, 'access_level': access_level}
            user_data[identifier] = user

            grouped_user_data = {level: {key: user_data[key] for key in user_data if user_data[key]['access_level'] == level} for level in range(1, 8)}

            with open(file_json, 'w') as f:
                json.dump(grouped_user_data, f, indent=4)

        print("Данные успешно обновлены и сохранены в файле 'user_data.json'")


update_user_data()