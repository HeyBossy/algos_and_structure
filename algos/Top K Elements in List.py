# Задача:
# Дан массив целых чисел nums и целое число k. Необходимо вернуть k наиболее часто встречающихся элементов в массиве.
# Предполагается, что для каждого набора тестовых данных ответ всегда уникален.

# Примеры:
# Пример 1:
# Ввод: nums = [1, 2, 2, 3, 3, 3], k = 2
# Вывод: [2, 3]

# Пример 2:
# Ввод: nums = [7, 7], k = 1
# Вывод: [7]

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # нужно найти ровно k самых частых элементов, независимо от того, сколько раз они встречаются.
        ans = []
        count = Counter(nums)
        for i, count in count.most_common(k):
            ans.append(i)
        return ans


# Примеры использования:
solution = Solution()

# Пример 1
print(solution.topKFrequent([1, 2, 2, 3, 3, 3], 2))  # Ожидаемый вывод: [2, 3]

# Пример 2
print(solution.topKFrequent([7, 7], 1))  # Ожидаемый вывод: [7]
