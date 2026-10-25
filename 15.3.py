from random import *

while True:
    try:
        n = int(input('Введите n - кол-во элементов списка (целое неотрицательное число): '))
        if n < 1:
            print('Ошибка: n должно быть целым неотрицательным числом')
            continue
        print('Число n:', n)
        break
    except ValueError:
        print('Ошибка: n должно быть целым неотрицательным числом')

while True:
    try:
        A = float(input('Введите число A (начало диапазона): '))
        print('Число A:', A)
        break
    except ValueError:
        print('Ошибка: A должно быть числом')

while True:
    try:
        B = float(input('Введите число B (конец диапазона): '))
        print('Число B:', B)
        break
    except ValueError:
        print('Ошибка: B должно быть числом')

k = []
c = 0
mx = 0
s = 0

for i in range(n):
    k.append(randint(-100, 100))

for x in k:
    s += x
    if x > mx:
        mx = x
        s = 0
    if B >= A:
        if (A <= x) and (x <= B):
            c += 1
    else:
        if (A >= x) and (x >= B):
                    c += 1


print('Исходный список:', k)
print('Кол-во элементов в диапазоне от A до B:', c)
print('Сумма элементов, расположенных после максимального элемента:', s)