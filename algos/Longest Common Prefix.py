Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Для каждой позиции символов в строках вы проверяете, совпадают ли символы на этой позиции во всех строках.
Если все символы совпадают, добавляете их в префикс.
Если хотя бы один символ не совпал, прекратите проверку, так как это означает, что строка больше не является общим префиксом.
  
pref = ''
strs = ["flower", "flow", "flight"]
i = 0

while i < len(strs):
    current_char = strs[0][i]  # Берем символ из первой строки
    
    # Сравниваем текущий символ с символом в остальных строках
    for s in strs:
        if s[i] != current_char:
            break
    else:# Если цикл завершился без break, то все строки совпали на этой позиции
        pref += current_char

    i += 1

pref
