# Напишите программу которая на вход принимает строку, и отслеживает, сколько раз каждый символ уже
# встречался. Количество повторов добавляется к символам с помощью постфика сформата _n.
# d g h t r g r h t j h b v f d s d f

string = 'd g h t r g r h t j h b v f d s d f'
print(string)

my_list = string.split()
# my_list_2 = my_list[:]
# print(my_list)
# print(my_list_2)

my_dict = {}
new_list = []

for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))
    else:
        new_list.append(letter)
print(' '.join(new_list))