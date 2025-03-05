# самый просто способ через сет интесекшн но его делать не будем 
 
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

nums1.sort()  # Сортируем оба массива для упорядоченного обхода
nums2.sort()

ans = []
i, j = 0, 0

# Используем два указателя для обхода обоих массивов
while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
        ans.append(nums1[i])
        i += 1
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        j += 1
