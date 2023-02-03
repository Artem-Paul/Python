# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
#  вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

"""
import random
orel = 0
reshka = 0
n = int(input('Введите количество монеток: '))
for ind in range (n):
    temp = random.randint(0, 1)
    print(temp)
    if temp == 0:
        orel += 1
    elif temp == 1:
        reshka += 1
if orel < reshka:
    print(f'Нужно перевернуть {orel}')
elif orel > reshka:
    print(f'Нужно перевернуть {reshka}')
elif orel == reshka:
    print('Одинаковое количество.')
"""

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате
# по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3


import math

s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение: '))

D = s**2 - 4*p
x1 = (s - math.sqrt(D)) / 2
x2 = (s + math.sqrt(D)) / 2

print(int(x1), int(x2))


print('Введите число S')
S = int(input())
print('Введите число P')
P = int(input())
for num1 in range(S-1):
    num2 = S - num1
    if num1*num2 == P:
        print(num1,num2)
        break


summa = int(input("Введите сумму чисел: "))
product = int(input("Введите произведение чисел: "))
x = (summa-int((summa**2-4*product)**0.5))//2
y = (summa+int((summa**2-4*product)**0.5))//2
print(f'{summa} {product} -> {x} {y}')


a = 2
b = 3
sum = a + b
pro = a * b
print(f"сумма -> {sum}\nПроизведение -> {pro}")

while(True):
    first = int(input("Первое число: "))
    second = int(input("Второе число: "))

    if (first == a and second == b) or (first == b and second == a):
        print("Вы угадали")
        break
    else:
        print("Вы не угадали, попробуйте ещё")



x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)


num1 = int(input('Задумайте первое число: '))
num2 = int(input('Задумайте второе число: '))

hint_sum = num1 + num2
hint_multy = num1 * num2
print(f'Сумма {hint_sum}, произведение {hint_multy}')
x = 0
y = 1
count = 1
for x in range(hint_sum):
    for y in range(hint_multy):
        if x + y == hint_sum and x * y == hint_multy and count == 1:
            print(f'Задуманные числа {x} и {y}')
            count += 1



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

'''
n = int(input('Введите число: '))
ex = 0
res = 0
while res < n:
    res = 2 ** ex
    ex += 1
    if res > n:
        break
    print(res)
'''    

n = int(input("Введите число: "))
m = 1
while m < n:
    print(m, end=' ')
    m = m * 2
