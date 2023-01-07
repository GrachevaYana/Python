# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: - 6782 -> 23     - 0,56 -> 11

number = input('Введите любое число: ')
try:
    def sumdigit(x):
        if float(x) < 0:
            x = float(x) * (-1)
        summa = 0
        for i in str(x):
            if i != '.':
                summa += int(i)
        return summa

    print(sumdigit(number))

except:
    print('Введенное значение не является числом')
