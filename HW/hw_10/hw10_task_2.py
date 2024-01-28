"""
На вход программе подаются два списка, каждый из которых содержит
10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел
в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists,
который будет сравнивать числа из вашего билета
из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.


class LotteryGame:
    def __init__(self, ticket_numbers, winning_numbers):
        self.ticket_numbers = set(ticket_numbers)  # Преобразуем в множество для удобства сравнения
        self.winning_numbers = set(winning_numbers)  # Также преобразуем в множество

    def compare_lists(self):
        matching_numbers = self.ticket_numbers.intersection(self.winning_numbers)
        matching_numbers_count = len(
            self.ticket_numbers.intersection(self.winning_numbers))
        if matching_numbers:
            return matching_numbers_count  # Возвращает колличество совпадающих чисел
        else:
            return "Совпадающих чисел нет."



ticket_numbers = [3, 8, 12, 17, 21, 25, 31, 36, 40, 45]
winning_numbers = [8, 21, 30, 41, 34, 27, 19, 12, 3, 7]

lottery = LotteryGame(ticket_numbers, winning_numbers)
result = lottery.compare_lists()

print(result)  # Выводит совпадающие числа или сообщение о их отсутствии
"""

from collections import Counter

class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        counter1 = Counter(self.list1)
        counter2 = Counter(self.list2)
        matching_numbers = list((counter1 & counter2).elements())
        matching_numbers_count = len(matching_numbers)
        if matching_numbers_count == 0:
            print("Совпадающих чисел нет.")
        else:
            print(f"Совпадающие числа: {matching_numbers} "
                  f"\nКоличество совпадающих чисел: {matching_numbers_count}")


#return print(f"Совпавшие числа: {matching_numbers} \nКоличество совпадающих чисел: {matching_numbers_count}")#matching_numbers, matching_numbers_count

# Пример использования
list1 = [3, 3, 12, 12, 21, 25, 31, 36, 40, 7]
list2 = [3, 3, 12, 12, 34, 27, 19, 12, 3, 7]

game = LotteryGame(list1, list2)
#matching_numbers, matching_numbers_count = game.compare_lists()
matching_numbers = game.compare_lists()

#print(f"Совпавшие числа: {matching_numbers[0]} \nКоличество совпадающих чисел: {matching_numbers[1]}")
#print(matching_numbers)
