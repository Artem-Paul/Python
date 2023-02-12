# Дана последовательность чисел. Получить список уникальных элментов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
for i in my_list:
    print(f'{i} встречается {my_list.count(i)}')
    if my_list.count(i) == 1:
        new_list.append(i)
print(my_list)
print(f'Уникальные элементы {new_list}')

# print([letter for letter in my_list if my_list.count(letter) == 1])
