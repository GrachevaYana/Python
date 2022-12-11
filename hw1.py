# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример: - 6 -> да   - 7 -> да   - 1 -> нет

weekend = [6,7]
workday = [1,2,3,4,5]
try:
    day = int(input('Введите число дня недели: '))
    if(not day in weekend and not day in workday):
        print('Error')
    elif(day in workday):
        print('False')
    else:
        print('True')
except:
    print('Введенное значение не является числом')