"""
2. Площадь
    Пользователь вводит стороны прямоугольника, выведите его площадь

    3. Периметр
    Пользователь вводит стороны прямоугольника, выведите его периметр
"""

a = float(input('Введите первую сторону прямоугольника: '))
b = float(input('Введите вторую сторону прямоугольника: '))

s = a * b
p = (a + b) * 2

print(f'Площадь прямоугольника = {s}, Периметр прямоугольника = {p}')