'''
Назначение:
Численное интегрирование методом левых прямоугольников
и методом трапеций.

Овчинникова Анастасия

Переменные:
a - начальное значение
b - конечное значение
N1, N2, n - количество итераций
x - аргумент подынтегральной функции
s - интеграл
h - длина одного шага
I1, I2, I3, I4 - интегралы, вычисленные разными способами или с разным шагом
eps - точность
i - служебная
'''
from math import log

def f(x):
    return 1/log(x)

def leftRectangle(f, a, b, N):
    s = 0
    h = (b-a)/N
    for i in range(1, N+1):
        s += f(a+1*h)
    s *= h
    return s

def trapeze(f, a, b, N):
    s = (f(a)+f(b))/2
    h = (b-a)/N
    for i in range(1,N):
        s += f(a+i*h)
    s *= h
    return s

def main():
    print()
    print(18*' '+'\u2502'+'{:^18.4f}'.format(N1)+\
                 '\u2502'+'{:^18.4f}'.format(N2))
    line = 2*(18*'\u2500'+'\u253C')+18*'\u2500'
    print(line)
    I1 = leftRectangle(f, a, b, N1)
    I2 = leftRectangle(f, a, b, N2)
    I3 = trapeze(f, a, b, N1)
    I4 = trapeze(f, a, b, N2)
    print('{:^18}'.format('Метод')+'\u2502'+\
          18*' '+'\u2502')
    print('{:^18}'.format('правых')+'\u2502'+\
          '{:^18.4f}'.format(I1)+'\u2502'
          '{:^18.4f}'.format(I1))
    print('{:^18}'.format('прямоугольников')+'\u2502'+\
          18*' '+'\u2502')
    print(line)
    print('{:^18}'.format('Метод')+'\u2502'+\
          '{:^18.4f}'.format(I3)+'\u2502'
          '{:^18.4f}'.format(I4))
    print('{:^18}'.format('трапеций')+'\u2502'+\
          18*' '+'\u2502')
    print()
    print()

#уточние для метода левых прямоугольников
def refinement(eps):
    n = 2
    while True:
        I1 = leftRectangle(f, a, b, n)
        I2 = leftRectangle(f, a, b, n*2)
        if I2 - I1 < eps:
            for i in range(n, n*2):
                I3 = leftRectangle(f, a, b, n)
                I4 = leftRectangle(f, a, b, n+1)
                if I4 - I3 <eps:
                    res = n + 1
                    break
            print('Чтобы достичь точности '+str(eps)+\
                  ' необходимо '+str(res)+' итераций. ')
            break
        n *= 2

def CatchIntError(c):
    if c.isdigit():
        c = int(c)
    else:
        print('Некорректный ввод')
        
def getInterval():
    a = input('Введите начальное значение: ')
    b = input('Введите конечное значение: ')

def getStep():
    print('Чтобы выйти, нажмите ENTER.')
    N1 = input('Введите N1: ')
    if N1 = '':
        return
    else:
        CatchIntError(N1)
    N2 = input('ведите N2: ')
    CatchIntError(N2)
    if type(N1) is str or type(N2) is str:
        getStep()
        

def getAll():
    getInterval()
    getStep()
    
main()

eps = float(input('Введите эпсилон: '))
refinement(eps)

input()
