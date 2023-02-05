# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

num = int(input('Введите размер списка '))

list = [round(uniform(0, 9), 3) for i in range(num)]
min = min(list, key=lambda i: float(i))
max = max(list, key=lambda i: float(i))
dif = (max - int(max)) - (min - int(min))

print(list)
print(max, min)
print(round(dif, 3))
