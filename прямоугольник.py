a = int(input('введите значение одной стороны: '))
b = int(input('введите значение второй стороны: '))
print('*' * a)
for i in range (b-2):
    print('*' + ' ' * (b - 2) + '*')
print('*' * a)