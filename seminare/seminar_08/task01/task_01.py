"""
📌Вспоминаем задачу 3 из прошлого семинара.
Мы сформировали текстовый файл с псевдо именами и произведением чисел.
📌 Напишите функцию, которая создаёт из созданного ранее файла новый
с данными в формате JSON.
📌 Имена пишите с большой буквы.
📌 Каждую пару сохраняйте с новой строки.
"""
import json

def create_json_from_text(input_file, output_file):
    data = {}

    with open(input_file, 'r', encoding='utf-8') as f:
        linse = f.readlines()
        for el in linse:
            name, numbers = el.strip().split(' - ')
            name = name.capitalize()
            data[name] = numbers

    with open(output_file, 'w', encoding='utf-8') as f_json:
        json.dump(data, f_json, indent=4)


create_json_from_text('task7_3.txt', 'task7_3.json')