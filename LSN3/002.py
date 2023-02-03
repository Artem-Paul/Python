# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
#  (сдвиг - циклический) на K элементов вправо, K – положительное число.

# numbers = [1, 2, 2, 3, 3, 4, 5]
# k = int(input())

# # for i in numbers:
# #     numbers[i] += k
# #     print(numbers[i])

# for i in numbers:
#     numbers.insert(0,1)

# print(numbers)


# a = input().split()
# k = int(input())
# k = k%len(a)
# if k<0:
#     k = abs(k)
#     print(*a[k:],end =' ')
#     print(*a[0:k])
#     exit()
 
# if k>=0:
#     k = abs(k)
#     print(*a[-k:],end =' ')
#     print(*a[0:-k])
#     exit()


numbers = [130, 44, 22, 311, 52353, 314, 5]
k = int(input())
for i in range(k):
    numbers.insert(0, '1')
print(numbers)


list_19 = [1, 2, 3, 4, 5]
k = 3
for i in range(k):
    list_19.append(list_19.pop(0))
print(list_19)


list_1 = [5, 4, 6, 7, 8, -10]
k = 3

list_result = list()
for i in range(k):
    list_result.append(list_1[len(list_1) - 1 - i])
    print(list_result)
print(1)
for i in range(len(list_1) - k):
    list_result.append(list_1[i])
    print(list_result)
print(list_result)
