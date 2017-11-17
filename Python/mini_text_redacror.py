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
    return log(x)

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

def printer(a, b, N1, N2):
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
          '{:^18.5f}'.format(I1)+'\u2502'
          '{:^18.5f}'.format(I2))
    print('{:^18}'.format('прямоугольников')+'\u2502'+\
          18*' '+'\u2502')
    print(line)
    print('{:^18}'.format('Метод')+'\u2502'+\
          '{:^18.5f}'.format(I3)+'\u2502'
          '{:^18.5f}'.format(I4))
    print('{:^18}'.format('трапеций')+'\u2502'+\
          18*' '+'\u2502')
    print()
    print()

#уточние для метода левых прямоугольников
def refinement(eps):
    n = 1
    while True:
        I1 = leftRectangle(f, a, b, n)
        I2 = leftRectangle(f, a, b, n*2)
        if abs(I2 - I1) < eps:
            for i in range(n, n*2):
                I3 = leftRectangle(f, a, b, n)
                I4 = leftRectangle(f, a, b, n+1)
                if I4 - I3 < eps:
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
    return c

def CatchFloatError(c):
    if c.isdigit():
        return float(c)
    else:
        n = ''
        nums = '0123456789-'
        for i in range(len(c)):
            if i != 0 and i != len(c) - 1 and c[i] in '0123456789':
                n += c[i]
            elif i == 0 and c[i] in nums:
                n += c[i]
            elif i == len(c)-1 and i != 0 and (c[i] in nums[0:10] or c[i] == '.'):
                n += c[i]
            elif i != 0 and i != len(c)-1 and c[i] == '.':
                if '.' not in n and 'e' not in n:
                    n += c[i]
            elif i != 0 and i != len(c)-1 and c[i] == '-':
                if c[i-1] == 'e':
                    n += c[i]
            elif i != 0 and i != len(c)-1 and c[i] == 'e':
                if 'e' not in n:
                    n += c[i]
            else:   
                break
        if len(n) == len(c) and len(n) != 0:
            n = float(n)
            return n
        else:
            print('Некорректный ввод. ')

N1 = input('Введите N1: ')
N1 = CatchIntError(N1)
if type(N1) is int:
    N2 = input('ведите N2: ')
    N2 = CatchIntError(N2)
    if type(N2) is int:
        a = input('Введите начальное значение: ')
        a = CatchFloatError(a)
    if type(a) is float:
        b = input('Введите конечное значение: ')
        b = CatchFloatError(b)
        if type(b) is float:
            if a >= b:
                print('Некорректный ввод. ')
            else:
                printer(a, b, N1, N2)
                eps = input('Введите эпсилон: ')
                eps = CatchFloatError(eps)
                if type(eps) is float:
                    refinement(eps)

'''if type(a) is float and type(b) is float\
   and type(N1) is int and type(N2) is int and b > a:'''
    


input()
