def find_combinations(items, max_weight):
    backpack = {}  # словарь для записи предметов в рюкзаке
    result = []  # список для хранения всех комбинаций

    def backtrack(curr_weight, curr_items):
        if curr_weight <= max_weight:
            result.append(
                curr_items.copy())  # добавляем текущую комбинацию в список результатов

        for item, weight in items.items():
            if item not in curr_items:  # если предмет уже есть в текущей комбинации, пропускаем его
                curr_items[
                    item] = weight  # добавляем предмет в текущую комбинацию
                curr_weight += weight  # увеличиваем суммарный вес текущей комбинации
                backtrack(curr_weight,
                          curr_items)  # рекурсивно вызываем функцию backtrack
                del curr_items[item]  # удаляем предмет из текущей комбинации
                curr_weight -= weight  # уменьшаем суммарный вес текущей комбинации

    backtrack(0, {})
    return result

result = find_combinations(items, max_weight)
print(result)
