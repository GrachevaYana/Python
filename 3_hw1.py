# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:    - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import Random, randint
n = int(input('Введите длину списка: '))
spisok = []
for i in range(n):
    spisok.append(randint(-10,11))
print(spisok)
print(f'Сумма элементов списка, стоящих на нечетных позициях, равна: {sum(spisok[1::2])}')