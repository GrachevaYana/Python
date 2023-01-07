# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)
from random import Random, randint

n = int(input('Введите число N: '))
spisok = []
for i in range(n):
    spisok.append(randint(-n,n+1))
print(spisok)

def mixnumber(spisok):
    list = spisok[:]
    spisok_length = len(list)
    for i in range(spisok_length):
        index = randint(0, spisok_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(mixnumber(spisok))