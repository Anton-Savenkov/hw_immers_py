"""
Допишите в вашу задачу Archive обработку исключений.

Добавьте исключение в ваш код InvalidTextError, которые будет вызываться,
когда текст не является строкой или является пустой строкой.

Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'

И InvalidNumberError, которое будет вызываться, если число не является
положительным целым числом или числом с плавающей запятой.

Текст ошибки: 'Invalid number: {введенное число}.
Number should be a positive integer or float.'
"""
#Проверенное решение

from typing import Union


class InvalidTextError(Exception):
    def __init__(self, text):
        self.text = text
        super().__init__(f"Invalid text: {text}. "
                         f"Text should be a non-empty string.")


class InvalidNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Invalid number: {number}. "
                         f"Number should be a positive integer or float.")


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self._validate_text(text)
        self._validate_number(number)
        self.text = text
        self.number = number

    def _validate_text(self, text: str):
        if not isinstance(text, str) or len(text) == 0:
            raise InvalidTextError(text)

    def _validate_number(self, number: Union[int, float]):
        if not ((isinstance(number, int) and number > 0) or (
                isinstance(number, float) and number > 0)):
            raise InvalidNumberError(number)

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

#пример вывода
archive1 = Archive("First Text", 1)

print(archive1)

archive2 = Archive("Second Text", 2)

print(archive2)

archive3 = Archive("Third Text", 3)

print(archive3)