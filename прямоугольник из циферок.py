a = int(input('введите значение длины: '))
b = int(input('введите значение высоты: '))
for i in range (1, b+1):
    for j in range (a):
        print((i, i + b * j) * j)
