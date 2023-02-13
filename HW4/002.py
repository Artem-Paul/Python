n = int(input('Введите кол-во элементов первого множества: '))
m = int(input('Введите кол-во элементов второго множества: '))
setOne = set()
setTwo = set()
print('Введите элементы первого множества: ')
for i in range(n):
    setOne.add(int(input()))
print('Введите элементы второго множества: ')
for i in range(m):
    setTwo.add(int(input()))
print(sorted(setOne.intersection(setTwo)))


