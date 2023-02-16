def sum_div(n):
    summa = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            summa += i
    return summa


summ_dict = {} # 284: 220,

k = int(input())
for number in range(2, k + 1):
    if number in summ_dict:
        if sum_div(number) == summ_dict[number]:
            print(number, summ_dict[number])
    summ_dict[sum_div(number)] = number