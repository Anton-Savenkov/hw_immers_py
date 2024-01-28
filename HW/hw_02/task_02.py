"""
На вход автоматически подаются две строки
frac1 и frac2 вида a/b - дробь с числителем и знаменателем.

Напишите программу, которая должна возвращать сумму и произведение дробей.

Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

frac1 = "5/7"
frac2 = "2/5"

#переводим числитель и знаменатель в int
n1 = int(frac1.split('/')[0])
n2 = int(frac2.split('/')[0])
d1 = int(frac1.split('/')[1])
d2 = int(frac2.split('/')[1])

#вывод результата
print(f'Cумма дробей: {n1 * d2 + n2 * d1}/{d1 * d2}')
print(f'Произведение дробей: {n1 * n2}/{d1 * d2}')

#проверка результато модулем Fraction
print(f'Сумма дробей:', Fraction(n1, d1) + Fraction(n2, d2))
print(f'Произведение дробей:', Fraction(n1, d1) * Fraction(n2, d2))



"""
Произведение дробей: 1/6

f_summ = (int(frac1[0]) / int(frac1[2])) + (int(frac2[0]) / int(frac2[2]))
print(f_summ)


frac_summ = Fraction(int(frac1[0]), int(frac1[2])) + \
            Fraction(int(frac2[0]), int(frac2[2]))
frac_mult = Fraction(int(frac1[0]), int(frac1[2])) * \
            Fraction(int(frac2[0]), int(frac2[2]))

print(f'Сумма дробей: {frac_summ}')
print(f'Произведение дробей: {frac_mult}')
"""

#Сумма дробей: 5/6
#Произведение дробей: 1/6
#Сумма дробей: 5/6
#Произведение дробей: 1/6
