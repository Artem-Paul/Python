# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список
# чисел пока не введут 0. Все числа списка находятся на разных строках.
# Ввод:          Вывод:
# 1 2 3 2 3      2

some_list = []
while True:
    number = int(input())
    if number == 0:
        break
    some_list.append(number)

count_dict = {}  # 2: 2, 3: 3, 4:1, 5:1

for el in some_list:
    if count_dict.get(el):
        count_dict[el] += 1
    else: 
        count_dict[el] = 1

print(count_dict)  

count = 0
for value in count_dict.values():
    count += value // 2 
print(count)