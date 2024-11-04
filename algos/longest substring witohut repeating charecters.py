# Задача:
# Дана строка s, необходимо найти длину самой длинной подстроки без повторяющихся символов.

# Примеры:
# Пример 1:
# Ввод: s = "abcabcbb"
# Вывод: 3
# Пояснение: Ответ "abc", с длиной 3.

# Пример 2:
# Ввод: s = "bbbbb"
# Вывод: 1
# Пояснение: Ответ "b", с длиной 1.

# Пример 3:
# Ввод: s = "pwwkew"
# Вывод: 3
# Пояснение: Ответ "wke", с длиной 3.
# Обратите внимание, что ответ должен быть подстрокой, а не подпоследовательностью.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Находит длину самой длинной подстроки без повторяющихся символов.

        Параметры:
        s (str): Исходная строка.

        Возвращает:
        int: Длина самой длинной подстроки без повторяющихся символов.
        """
        val = ''  # Временная строка для хранения текущей подстроки без повторов
        len_slt = {}  # Словарь для хранения длины подстрок без повторов

        # Проходим по каждому символу строки
        for index, char in enumerate(s):
            val += char  # Добавляем символ к текущей подстроке

            # Если символ уже есть в текущей подстроке, обрезаем подстроку до символа
            if val.count(char) > 1:
                cut_index = val.index(char)
                val = val[cut_index + 1:]

            # Обновляем длину подстроки в словаре
            len_slt[val] = len(val)

        # Возвращаем максимальную длину подстроки без повторов
        return max(len_slt.values()) if len_slt else 0


# Примеры использования:
solution = Solution()

# Пример 1
print(solution.lengthOfLongestSubstring("abcabcbb"))  # Ожидаемый вывод: 3

# Пример 2
print(solution.lengthOfLongestSubstring("bbbbb"))  # Ожидаемый вывод: 1

# Пример 3
print(solution.lengthOfLongestSubstring("pwwkew"))  # Ожидаемый вывод: 3
