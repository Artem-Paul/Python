# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
#  и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
#  an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

'''
a = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('Введите разность: '))
n = int(input('Введите количество элементов прогрессии: '))
list = []

for i in range (1, n):
    list.append(a + (i-1) * d)
    
print(list)
'''

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

min = int(input('Введите минимум: '))
max = int(input('Введите максимум: '))
list = [11, 24, 25, 9, 44, 56, 96, 38]

for i in range (0, len(list)):
    if min < list[i] < max:
        print(i)