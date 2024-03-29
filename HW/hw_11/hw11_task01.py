"""
Разработайте программное обеспечение для ведения журнала событий.
Вам необходимо создать класс, который будет представлять строки журнала
и включать в себя информацию об авторе и времени создания каждой записи.

Условие задачи:

Создайте класс MyStr, который наследуется от встроенного класса str
и добавлять дополнительную информацию о создателе строки и времени ее создания.
Этот класс будет представлять строки с информацией о событиях.

Класс MyStr должен иметь следующие атрибуты и методы:

value (str): Строковое значение с описанием события.
author (str): Имя автора, создавшего запись.
time: Время создания записи в формате '%Y-%m-%d %H:%M'.

Магические методы (Dunder-методы):

Реализуйте метод __new__(cls, value, author), который создает новый объект
класса MyStr с заданным value и author. Метод также автоматически
фиксирует время создания записи. В этом методе создается новый объект MyStr
с указанными атрибутами и текущим временем в атрибуте time.

Реализуйте метод __str__(self), который возвращает строковое представление
объекта класса MyStr с информацией о событии, авторе и времени создания.

Реализуйте метод __repr__(self), который возвращает строковое представление
объекта класса MyStr.
Метод __repr__ возвращает строку, которая может быть использована для
создания точно такого же объекта MyStr с теми же значениями value и author`.

"""

from datetime import datetime

class MyStr(str):
    def __new__(cls, value, author):
        obj = super().__new__(cls, value)
        obj.author = author
        obj.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return obj

    def __str__(self):
        return f"{str.__str__(self)} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self):
        return f"MyStr({str.__repr__(self)}, {self.author!r})"

# Пример использования
event = MyStr("Завершилось тестирование", "Jaaaaahn")
print(event)

my_string = MyStr("Пример текста", "Иван")
print(my_string)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))