n = int(input('введите свое любимое число и узнайте его простые делители: '))
for a in range(2, n+1):
    if n % a == 0:
        for i in range(2, a):
            if a % i == 0:
                break
        else:
            print(a)
