# Задача:
# Дан массив строк strs. Необходимо сгруппировать все анаграммы вместе в виде подсписков.
# Анаграмма — это строка, которая содержит те же символы, что и другая строка, но в другом порядке.

# Примеры:
# Пример 1:
# Ввод: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
# Вывод: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

# Пример 2:
# Ввод: strs = ["x"]
# Вывод: [["x"]]

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Группирует все анаграммы в массиве строк strs.

        Параметры:
        strs (List[str]): Массив строк.

        Возвращает:
        List[List[str]]: Список подсписков, где каждая группа состоит из анаграмм.
        """
        # Сортируем символы каждой строки для упрощения сравнения
        sorted_strs = [''.join(sorted(word)) for word in strs]
        new_str = []  # Результирующий список для групп анаграмм
        seen = set()  # Множество для отслеживания уже обработанных групп анаграмм

        # Проходим по каждому отсортированному слову и группируем анаграммы
        for i, word in enumerate(sorted_strs):
            if sorted_strs.count(word) > 1 and word not in seen:
                # Находим индексы текущей группы анаграмм
                ind = [j for j, char in enumerate(sorted_strs) if char == word]
                words = [strs[j] for j in ind]
                new_str.append(words)
                seen.add(word)  # Помечаем эту группу анаграмм как обработанную
            elif sorted_strs.count(word) == 1:
                # Добавляем одиночное слово в виде списка
                new_str.append([strs[i]])

        return new_str  # Возвращаем результат после завершения цикла

# Примеры использования:
solution = Solution()

# Пример 1
print(solution.groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
# Ожидаемый вывод: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

# Пример 2
print(solution.groupAnagrams(["x"]))  # Ожидаемый вывод: [["x"]]
