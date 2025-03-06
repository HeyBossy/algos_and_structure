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


s = "abcabcbbdfg"
# right — расширяет окно, добавляя новые символы.
# left — сдвигается вперёд, чтобы убрать повторяющийся символ, когда он встречается.
left, right = 0, 0
max_length = 0
char_set = set()
dict_char = {}
while right < len(s):
    if s[right] not in char_set:
        # Если символ s[right] уникален для текущего окна,
        # добавляем его в множество и расширяем окно вправо.
        char_set.add(s[right])
        # Обновляем максимальную длину, учитывая текущее окно от left до right.
        max_length = max(max_length, right - left + 1)
        dict_char[s[left:right+1]] = max_length # если хотим сохранить словарик 
        right += 1
    else:
        # Если s[right] уже есть в окне, значит, окно содержит повтор.
        # Убираем символ s[left] из окна и сдвигаем левый указатель вправо.
        char_set.remove(s[left])
        left += 1
max(dict_char.values())


# скользящее окно
 char_set = set()  # Хранит уникальные символы в окне
    left = 0  # Левый указатель окна
    max_length = 0

    for right in range(len(s)):  # Двигаем правый указатель
        while s[right] in char_set:  # Пока символ уже есть в окне
            char_set.remove(s[left])  # Удаляем символ слева
            left += 1  # Сдвигаем левый указатель
        char_set.add(s[right])  # Добавляем новый символ в окно
        max_length = max(max_length, right - left + 1)  # Обновляем максимум

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

