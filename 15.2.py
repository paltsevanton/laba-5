import string

A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
B = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = str(input('Введите строку: '))
b = ''
k = []
c = 0

for x in range(len(a)):
    k.append(x)

for i in a:
    if i in A:
        b += B[c]
    else:
        b += str(k[c])
    c += 1
    

print(a)
print(b)
