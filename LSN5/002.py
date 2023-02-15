# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import time
magazine = [int(input('Введите оценку: ')) for _ in range (int(input('Введите кол-во оценок')))]
# list comprehension 

start = time.perf_counter()
maxx = max(magazine)
minn = min(magazine)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
minn = magazine[0]
maxx = magazine[0]
for el in magazine:
    if el < minn:
        minn = el
    elif el > maxx:
        maxx = el
end = time.perf_counter()
print(end - start)
print(magazine)

for ind in range(0, len(magazine)):
    if magazine[ind] == maxx:
        magazine[ind] = minn
print(magazine)