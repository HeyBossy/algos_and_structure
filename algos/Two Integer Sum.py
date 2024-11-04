# Задача:
# Дан массив целых чисел nums и целое число target. Необходимо найти индексы i и j, такие что nums[i] + nums[j] == target и i != j.
# Предполагается, что для каждого входного массива существует ровно одна пара индексов i и j, удовлетворяющих этому условию.
# Возвращаемый ответ должен содержать меньший индекс первым.

# Примеры:
# Пример 1:
# Ввод: nums = [3, 4, 5, 6], target = 7
# Вывод: [0, 1]
# Пояснение: nums[0] + nums[1] == 7, поэтому возвращаем [0, 1].

# Пример 2:
# Ввод: nums = [4, 5, 6], target = 10
# Вывод: [0, 2]

# Пример 3:
# Ввод: nums = [5, 5], target = 10
# Вывод: [0, 1]

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_uppend = []
        for start in range(len(nums)):
            end = len(nums) - 1
            while start < end:
                current_sum = nums[start] + nums[end]
                if current_sum == target:
                    ans_uppend = [start, end]
                    break
                else:
                    end -= 1
        return ans_uppend


# Примеры использования:
solution = Solution()

# Пример 1
print(solution.twoSum([3, 4, 5, 6], 7))  # Ожидаемый вывод: [0, 1]

# Пример 2
print(solution.twoSum([4, 5, 6], 10))    # Ожидаемый вывод: [0, 2]

# Пример 3
print(solution.twoSum([5, 5], 10))       # Ожидаемый вывод: [0, 1]
