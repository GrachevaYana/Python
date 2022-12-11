# 2.Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры: - 1, 4, 8, 7, 5 -> 8     - 78, 55, 36, 90, 2 -> 90
numbers = []
for i in range(5):
    numbers.append(int(input(f'Введите {i+1} число: ')))
    print(numbers[i])
print(numbers)
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(f'Максимальное число {max}')

