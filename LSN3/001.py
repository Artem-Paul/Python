# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = list(set(numbers))
print(len(unique_numbers))
