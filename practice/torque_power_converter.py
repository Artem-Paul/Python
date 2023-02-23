torq = float(input('Введите момент: '))
rpm = float(input('Введите обороты: '))
power = (torq * 0.7375610331755 * rpm) / 5252
print(f'Мощность л.с.: {power}')