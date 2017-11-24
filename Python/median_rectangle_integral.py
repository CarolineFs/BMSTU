N = int(input('Введите N: '))
a = float(input('Введите начальное значение: '))
b = float(input('Введите конечное значение: '))

def f(x):
    return x*x


def middleRect(f,a,b,N):
    s = 0
    h = (b-a)/N
    for i in range(N):
        s += f(a+i*h+h/2)
    s *= h
    return s


I = middleRect(f, a, b, N)
print()
print('Интеграл: ', '{:0.4f}'.format(I))

    
