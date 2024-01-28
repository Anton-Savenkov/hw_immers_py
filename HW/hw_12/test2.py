import csv

class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not value.istitle() or not value.replace(" ", "").isalpha():  # Добавим возможность писать ФИО через пробел
            raise ValueError(f"ФИО должно состоять только из букв и начинаться с заглавной буквы")
        instance.__dict__[self.name] = value

class SubjectDescriptor:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not hasattr(instance, 'subjects_list'):
            with open(instance.subjects_file, newline='', encoding='utf-8') as csvfile:
                subject_reader = csv.reader(csvfile)
                instance.subjects_list = next(subject_reader)
        if value not in instance.subjects_list:
            raise ValueError(f"Предмет {value} не найден")
        instance.__dict__[self.name] = value

class Student:
    name = NameDescriptor()
    subjects = SubjectDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects_file = subjects_file
        self.subjects = {}

    def load_subjects(self, subjects_file):
        with open(subjects_file, newline='', encoding='utf-8') as csvfile:
            subject_reader = csv.reader(csvfile)
            self.subjects_list = next(subject_reader)

    def add_grade(self, subject, grade):
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise ValueError("Оценка должна быть целым числом от 2 до 5")
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if not isinstance(test_score, int) or test_score < 0 or test_score > 100:
            raise ValueError("Результат теста должен быть целым числом от 0 до 100")
        if subject not in self.subjects:
            self.subjects[subject] = {'grades': [], 'test_scores': []}
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects:
            return 0.0
        scores = self.subjects[subject]['test_scores']
        if scores:
            return sum(scores) / len(scores)
        else:
            return 0.0

    def get_average_grade(self):
        all_grades = [grade for subject_grades in self.subjects.values() for grade in subject_grades['grades']]
        if all_grades:
            return sum(all_grades) / len(all_grades)
        else:
            return 0.0

    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.subjects.keys())}"

# Пример использования
student = Student("Иван Иванов", "subjects.csv")

student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)

student.add_grade("История", 5)
student.add_test_score("История", 92)

average_grade = student.get_average_grade()
print(f"Средний балл: {average_grade}")

average_test_score = student.get_average_test_score("Математика")
print(f"Средний результат по тестам по математике: {average_test_score}")

print(student)