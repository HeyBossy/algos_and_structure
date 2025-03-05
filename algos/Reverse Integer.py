Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            new_x = -int(str(abs(x))[::-1])  # Для отрицательного числа делаем реверс и восстанавливаем знак
        else:
            new_x = int(str(abs(x))[::-1])  # Для положительного числа просто делаем реверс
        
        # Проверка на переполнение 32-битного целого числа
        if new_x < -2**31 or new_x > 2**31 - 1:
            return 0
        
        return new_x
