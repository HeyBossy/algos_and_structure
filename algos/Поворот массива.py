Вход: nums = [1,2,3,4,5,6,7], k = 3
 Выход: [5,6,7,1,2,3,4]
 Пояснение:
повернуть на 1 шаг вправо: [7,1,2,3,4,5,6]
повернуть на 2 шага вправо: [6,7,1,2,3,4,5]
повернуть на 3 шага вправо: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # сдвиг на k % n шагов
        easy_ans = nums[-k:]+nums[:-k]

        # через циклы 
        n = len(nums)
        k = k % n  # сдвиг на k % n шагов, чтобы избежать лишних сдвигов
        for _ in range(k):
            last_element = nums[-1]
            for i in range(n-1, 0, -1):  # Перемещаем элементы вправо
                nums[i] = nums[i-1]
            nums[0] = last_element  # Ставим последний элемент на первое место 
        return easy_ans
        
