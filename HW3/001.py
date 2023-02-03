# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# array = [2, 3, 5, 9, 3]

'''
int_array = []
for element in input().split():
    int_array.append(int(element))

sum = 0
for i in range(0, len(int_array)):
    if i % 2 != 0:
        sum = sum + int_array[i] 
    
print(sum)
'''

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

'''
int_array = []
for element in input().split():
    int_array.append(int(element))

multiply_array = []
for i in range(0, len(int_array)):
    multiply_array[i] = int_array[i] * int_array[len - 1 - i]

print(multiply_array)
'''

# array = [2, 3, 4, 5, 6]
# new_array = []
# for i in range(0, len(array)):
#     new_array.append(array[i] * array[len - 1 - i])
# print(new_array)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
#  и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

'''
array = [1.1, 1.2, 3.1, 5, 10.01]
dec = 0
maxDec = 0
minDec = 1
for i in range(0, len(array)):
    dec = array[i] % 1
    if array[i] % 1 == 0:
        continue
    elif dec < minDec:
        minDec = dec
    elif dec > maxDec:
        maxDec = dec

print(round(maxDec, 2) - round(minDec, 2))
'''