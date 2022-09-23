a = int(input('введите значение одной стороны: '))
b = int(input('введите значение второй стороны: '))
for i in range (1, b+1):
    for j in range (i, a*b+1, b):
        print(j)
#не работает как надо
