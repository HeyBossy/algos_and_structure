# Задача:
# Даны две строки s и t. Необходимо вернуть True, если строки являются анаграммами друг друга, иначе вернуть False.

# Определение анаграммы:
# Анаграмма — это строка, содержащая те же символы, что и другая строка, но в другом порядке.

# Примеры:
# Пример 1:
# Ввод: s = "racecar", t = "carrace"
# Вывод: True

# Пример 2:
# Ввод: s = "jar", t = "jam"
# Вывод: False

from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Проверяет, являются ли две строки анаграммами друг друга.

        Параметры:
        s (str): Первая строка.
        t (str): Вторая строка.

        Возвращает:
        bool: True, если строки являются анаграммами, иначе False.
        """
        # красиво решение : Counter(s) == Counter(t)
        # Если длины строк не равны, сразу возвращаем False
        if len(s) != len(t):
            return False

        # Подсчёт символов в строке s
        char_index_s: Dict[str, int] = {}
        for char_s in s:
            if char_s not in char_index_s:
                char_index_s[char_s] = 1
            else:
                char_index_s[char_s] += 1

        # Подсчёт символов в строке t
        char_index_t: Dict[str, int] = {}
        for char_t in t:
            if char_t not in char_index_t:
                char_index_t[char_t] = 1
            else:
                char_index_t[char_t] += 1

        # Проверка, равны ли словари подсчёта символов
        return char_index_s == char_index_t

# Примеры использования:
solution = Solution()

# Пример 1
print(solution.isAnagram("racecar", "carrace"))  # Ожидаемый вывод: True

# Пример 2
print(solution.isAnagram("jar", "jam"))          # Ожидаемый вывод: False
