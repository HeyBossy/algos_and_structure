# Задача:
# Разработайте алгоритм для кодирования списка строк в одну строку. Закодированная строка затем должна быть декодирована обратно в исходный список строк.

# Примеры:
# Пример 1:
# Ввод: ["neet", "code", "love", "you"]
# Вывод: ["neet", "code", "love", "you"]

# Пример 2:
# Ввод: ["we", "say", ":", "yes"]
# Вывод: ["we", "say", ":", "yes"]

from typing import List
##########encode - длина слова - # - само слово
s = ["neet", "code", "love", "you"]
encode_s = []
for char in s:
    new_word = f'{len(char)}#{char}' 
    encode_s.append(new_word)
encode_s


###### находим решетку и длину излвекаем и затем само слово
decode_s = []
for dec_char in encode_s:
    j = dec_char.find('#')
    lenght = int(dec_char[:j])
    word = dec_char[j+1:j+1+lenght]
    decode_s.append(word)
decode_s    


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Кодирует список строк в одну строку.

        Параметры:
        strs (List[str]): Список строк для кодирования.

        Возвращает:
        str: Закодированная строка. типо #длина слова потом слово потом # длина другого слово и след слово
        """
        new_s = ''
        for word in strs:
            len_str = f'{len(word)}'  # Длина слова в виде строки
            new_s += len_str + '#' + word  # Добавляем длину, разделитель и само слово
        return new_s

    def decode(self, dec_str: str) -> List[str]:
        """
        Декодирует строку обратно в исходный список строк.

        Параметры:
        dec_str (str): Закодированная строка.

        Возвращает:
        List[str]: Исходный список строк.
        """
        decoded_list = []
        i = 0
        while i < len(dec_str):
            # Найти позицию символа `#`, который отделяет длину от слова
            j = dec_str.find('#', i)
            # Извлекаем длину слова
            len_word = int(dec_str[i:j])
            # Переходим к началу слова после символа `#`
            i = j + 1
            # Извлекаем слово по его длине
            append_word = dec_str[i:i + len_word]
            # Добавляем слово в список
            decoded_list.append(append_word)
            # Обновляем индекс `i` для перехода к следующей закодированной части
            i += len_word
        return decoded_list

# Примеры использования:
solution = Solution()

# Пример 1
encoded = solution.encode(["neet", "code", "love", "you"])
print("Encoded:", encoded)  # Закодированная строка
decoded = solution.decode(encoded)
print("Decoded:", decoded)  # Ожидаемый вывод: ["neet", "code", "love", "you"]

# Пример 2
encoded = solution.encode(["we", "say", ":", "yes"])
print("Encoded:", encoded)  # Закодированная строка
decoded = solution.decode(encoded)
print("Decoded:", decoded)  # Ожидаемый вывод: ["we", "say", ":", "yes"]
