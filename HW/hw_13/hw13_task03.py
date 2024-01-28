"""
В организации есть два типа людей: сотрудники и обычные люди.
Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая)
Отчество (строка, не пустая) Возраст (целое положительное число)
Сотрудники имеют также уникальный идентификационный номер (ID),
который должен быть шестизначным положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для управления
данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять
валидность входных данных и генерировать исключения
InvalidNameError и InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person
и добавлять уникальный идентификационный номер (ID).
Класс Employee также должен проверять валидность
ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person,
который будет увеличивать возраст человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень
сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными
и проверить, что исключения работают корректно при передаче неверных данных.
"""
#Поверенное решение
class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, name, surname, patronymic, age):
        self._validate_name(name, "Name")
        self._validate_name(surname, "Surname")
        self._validate_name(patronymic, "Patronymic")
        self._validate_age(age)
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def _validate_name(self, value, field):
        if not isinstance(value, str) or not value:
            raise InvalidNameError(f"Invalid {field.lower()}: {value}. {field} should be a non-empty string.")

    def _validate_age(self, age):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, surname, name, patronymic, age, employee_id):
        super().__init__(surname, name, patronymic, age)
        self._validate_id(employee_id)
        self.employee_id = employee_id

    def _validate_id(self, employee_id):
        if not isinstance(employee_id, int) or employee_id < 100000 or employee_id > 999999:
            raise InvalidIdError(f"Invalid id: {employee_id}. Id should be a 6-digit positive integer between 100000 and 999999.")

    def get_level(self):
        return sum(int(digit) for digit in str(self.employee_id)) % 7

# Проверка на примерах:
try:
    person1 = Person("", "John", "Doe", 30)  # Неверное имя
except InvalidNameError as e:
    print(f"InvalidIdError: {str(e)}")

try:
    person2 = Person("Alice", "Smith", "Johnson", -5)  # Отрицательный возраст
except InvalidAgeError as e:
    print(f"InvalidIdError: {str(e)}")

try:
    employee = Employee("Bob", "Johnson", "Brown", 40, 12345)  # Неверный ID
except InvalidIdError as e:
    print(f"InvalidIdError: {str(e)}")

person3 = Person("Alice", "Smith", "Johnson", 25)
print(person3.get_age())  # Получить возраст


