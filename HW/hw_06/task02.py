"""
Добавьте в пакет, созданный на семинаре шахматный модуль.
Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
функцию is_attacking(q1,q2), проверяющую,
бьют ли ферзи друг друга и check_queens(queens),
которая проверяет все возможные пары ферзей.
Известно, что на доске 8×8 можно расставить 8 ферзей так,
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел,
каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Не забудьте напечатать результат.
"""
queens = [(1, 6), (2, 3), (3, 7), (4, 2), (5, 8), (6, 5), (7, 1), (8, 4)]

def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(
            q1[1] - q2[1]):
        return True
    else:
        return False


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


print(check_queens(queens))


# from itertools import combinations
#
# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])
#
# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True

