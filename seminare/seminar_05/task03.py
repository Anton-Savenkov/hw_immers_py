"""
 Задание No3
✔ Продолжаем развивать задачу 2.
✔ Возьмите словарь, который вы получили.
Сохраните его итераторатор.
✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

"""
data = 'произвольный текст для задания'
#my_dict = {el: ord(el) for el in data}

my_iter = iter({el: ord(el) for el in data}.items())

for el in range(5):
    print(next(my_iter))

print('new line')
print(next(my_iter))
