# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

k = int(input('Сколько чисел будем суммировать: '))

def numbers(k):
    sum = 0
    for i in range(k):
        n = int(input(f'Введи {i + 1} число: '))
        n = (1+1/n)**n
        sum = n + sum
        i += 1
    return sum

print('Сумма чисел равна: ',round((numbers(k)), 1))