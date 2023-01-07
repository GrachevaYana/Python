# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import Random, randint
n = int(input('Введите количество элементов списка: '))
spisok = []
spisoksumoddposition = []

for i in range(n):
    spisok.append(randint(0,5))
print(spisok)

for i in range(len(spisok)):
    while i < len(spisok) / 2 and n > len(spisok) / 2:
        n = n - 1
        m = spisok[i] * spisok[n]
        spisoksumoddposition.append(m)
        i += 1
print(spisoksumoddposition)