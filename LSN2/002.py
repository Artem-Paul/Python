# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

n = int(input("Введите число: "))
sum = 1
while (n > 0):
    sum = n*sum
    n = n-1
print(sum)

# n = int(input())
# fact = 1
# i = 2
# while i <= n:
#     fact *= i
#     i += 1
# print(fact)
