# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from random import randint
n = int(input("Введите число: "))
i = 2
spisok = []
n1 = n
while i <= n:
    if n % i == 0:
        spisok.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {n1}: {set(spisok)}")