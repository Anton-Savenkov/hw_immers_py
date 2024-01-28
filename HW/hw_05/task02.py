"""
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int, премия str
с указанием процентов вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии
в качестве значения.

Сумма рассчитывается как ставка умноженная на процент премии.

Не забудьте распечатать в конце результат.
"""
names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]
#bonuses = {el_1: el_2 * float(el_3.rstrip("%")) / 100 for el_1, el_2, el_3 in zip(names, salary, bonuses)}

print({el_1: el_2 * float(el_3.rstrip("%")) / 100 for el_1, el_2, el_3 in zip(names, salary, bonus)})



