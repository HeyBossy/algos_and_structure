3. Задача: Наибольшая общая подпоследовательность (Longest Common Subsequence)
Описание:
Даны две строки text1 и text2. Нужно найти длину их наибольшей общей подпоследовательности.

Пример:

python
Копировать
text1 = "abcde"
text2 = "ace"
Ожидаемый вывод:

python
Копировать
3
Объяснение: Наибольшая общая подпоследовательность: "ace".

text1 = "abcdef"
text2 = "acef"
# set_text1 = set(','.join(letter for letter in text1).split(',')) # O(1)
# set_text2 = set(','.join(letter for letter in text2).split(',')) # O(1)
# (set_text1.intersection(set_text2)) #O(1)
i, j = 0,0
ans = []
for i in range(len(text1)-1): #O(n)
  for j in range(len(text2)-1): #O(m)
    if text1[i]==text2[j]:
      ans.append(text1[i])
# СЛожнось алгоритма O(n*m)

ans
