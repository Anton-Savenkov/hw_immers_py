from datetime import datetime


class MyStr(str):
    def __new__(cls, value, author):
        obj = super().__new__(cls, value)
        obj.author = author
        obj.time = datetime.now().strftime('%Y-%m-%d %H:%M')
        return obj

    def __str__(self):
        if hasattr(self, 'formatted_time'):
            return f"{str.__str__(self)} (Author: {self.author}, Time of Creation: {self.formatted_time})"
        else:
            return f"{str.__str__(self)} (Aгthor: {self.author}, Time of Creation: [в формате '%Y-%m-%d %H:%M'])"

    def __repr__(self):
        return f"MyStr({str.__repr__(self)}, {self.author!r})"

    @property
    def formatted_time(self):
        try:
            return datetime.strptime(self.time, '%Y-%m-%d %H:%M').strftime(
                '%Y-%m-%d %H:%M')
        except ValueError:
            return None


# Example usage
event = MyStr("Завершилось тестирование", "John")
print(event)

my_string = MyStr("Пример текста", "Иван")
print(my_string)

my_string = MyStr("Мама мыла раму", "Маршак")
print(repr(my_string))
