Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

# Да, если вы не указываете ни start, ни stop в срезе с шагом -1, то срез будет включать и начало, и конец массива (или списка) включительно.
s = ["h","e","l","l","o"]
s[::-1] # s[start:stop:step] - 
s[-1::-1]  # от конца до последнего элемента сстоп типо не указали

ИЛИ 
s = ["h","e","l","l","o"]
left, right = 0, len(s)-1
while left < right:
    s[left], s[right] = s[right], s[left]
    left +=1
    right -=1
