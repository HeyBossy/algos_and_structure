# Задача:
# Дан массив целых чисел nums. Необходимо вернуть True, если в массиве есть хотя бы одно повторяющееся значение.
# В противном случае вернуть False.

# Примеры:
# Пример 1:
# Ввод: nums = [1, 2, 3, 3]
# Вывод: True

# Пример 2:
# Ввод: nums = [1, 2, 3, 4]
# Вывод: False

from typing import List



nums = [1, 2, 3, 4] 
dict_index = set()
for i in range(len(nums)):
    if nums[i] not in dict_index:
        dict_index.add(nums[i])

if len(list(dict_index))!= len(nums):
    print(False)
else: 
     print(True)
# тут алогоритм имеет сложност (O(n)
# Цикл for проходит по nums, что даёт O(N).
# set.add() и set.__contains__() выполняются за O(1) (в среднем).
# Проверка len(set) != len(nums) занимает O(1).

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Проверяет, содержит ли массив дублирующиеся значения.

        Параметры:
        nums (List[int]): Массив целых чисел.

        Возвращает:
        bool: True, если есть дублирующиеся значения, иначе False.
        """
        chat_index = {}  # Словарь для отслеживания элементов
        val = False  # Переменная для хранения результата

        for i in range(len(nums)):
            # Проверяем, если элемент еще не встречался, добавляем его в словарь
            if nums[i] not in chat_index:
                chat_index[nums[i]] = i
            else:
                # Если элемент уже в словаре, устанавливаем val в True и выходим из цикла
                val = True
                break

        return val

# Примеры использования:
solution = Solution()

# Пример 1
print(solution.hasDuplicate([1, 2, 3, 3]))  # Ожидаемый вывод: True

# Пример 2
print(solution.hasDuplicate([1, 2, 3, 4]))  # Ожидаемый вывод: False
