# Пользователь вводит строки, пока не введте пустую, гарантируется, что в строках лежат только цифры, 
# Найти сумму введенных чисел которые кратны 4

summa = 0
while True:
    a = input()
    if a == '':
        break
    if int(a) % 4 == 0:
        summa += int(a)
print(summa)