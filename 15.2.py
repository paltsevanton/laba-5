a = str(input('Введите текст: '))
b = str(input('Введите символ для удаления кго из текста: '))
c = ''

for i in a:
    if i == b:
        pass
    else:
        c += i

print('Исходный текст:', a)
print('Сжатый текст:', c)