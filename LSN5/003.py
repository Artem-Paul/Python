# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

'''
n = int(input())
# flag = False
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print('Число не является простоым')
        # flag = True
        break
# is not flag:
else: 
    print('простое')
'''
def simple(n):

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'Число не является простым'
    return 'простое'

for i in range (1, 20):
    print(i, simple(i))