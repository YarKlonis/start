a = int(input('введите свое любимое число и узнайте простое ли оно: '))
if a > 1:
    for i in range(2,a):
        if a % i ==0:
            print('оно не простое')
            break
    else:
        print('оно простое')
else:
    print('оно не такое простое')
