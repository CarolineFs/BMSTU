'''Назначение:
Вычисление таблицы значений функций.
Построение графика одной из функцийю.

Овчинникова Анастасия

Переменые:
x -начальное значение агрумента, изменяющееся в цикле
step - шаг
last - конечное значение аргумента
k2 - количество отрицательных значений q2
k1 -количество отрицательных значений q1
q1, q2, q3 - функции
i, j - служебная переменная
f - флаговая переменная
arg - количество шагов = step от начального значения до конечного
max1 - максимальное значение функции q1
max2 - максимальное значение функции q2
'''

from math import sqrt, copysign

first = float(input('Введите начальное значение аргумента: '))
step = float(input('Введите длину шага: '))
last = float(input('Введите конечное значение агрумента: '))

x = first
arg = int(abs((last-x)//step)) + 1
k1 = 0
k2 = 0
max1 = copysign(abs(x)**abs(x), x) + 2*x - 6
max2 = x**3 - x - 1
   
print('\n   x\t*','       q1', '\t*       q2', '\t*  q3')
print(49*'*')

for i in range(arg):
    q1 = copysign(abs(x)**abs(x), x) + 2*x - 6
    if q1 < 0:
        k1 += 1
    if q1 > max1:
        max1 = q1
    q2 = x**3 - x - 1
    if q2 < 0:
        k2 += 1
    if q2 > max2:
        max2 = q2
    q3 = sqrt(abs(q1*q2))
    print ('{:0.3f}'.format(x), '\t*  {:0.3f}'.format(q1),\
           '\t*  {:0.3f}'.format(q2), '\t*  {:0.3f}'.format(q3))
    x += step
print('\nКоличество отрицательных значений функции q2 = ', k2)
    
f = 0
x = round(first, 7)
max1 = round(max1)
max2= round(max2)
    
if k2 > 0 or (k1 == 0 and k2 == 0):
    print('\nГрафик функции q2 = x^3 - x - 1: \n')
    m = 27
    s = ((arg//2+1)+m)*'\u0000'
    if max2 > (arg//2+1)+m:
        m = max2
        s = m*'\u0000'
    for i in range(arg):
        q2 = round(x**3 - x - 1)
        if x < 0:
            if q2 < 0:
                q2 *= -1
                print('{:0.3f} '.format(x)+(len(s)-q2-1)*' '+'*'+(q2-1)*' '+'\u2502')
            elif q2 == 0:
                print('{:0.3f} '.format(x)+(len(s)-1)*' ')
            elif q2 > 0:
                q2 *= -1
                print('{:0.3f} '.format(x)+s+'\u2502'+(len(s)-q2-1)*' '+'*')
        elif x >= 0:
            if x == 0:
                f = 1
                if q2 > 0:
                    q2 *= -1
                    print('x      ', (len(s)-2)*'\u2500'+'\u253C'+(q2-1)+'\u2500'+'*'+(len(s)-q2-2)*'\u2500'+' y')
                elif q2 == 0:
                    print('x      ', (len(s)-2)*'\u2500'+'\u253C'+'*'+(len(s)-2)*'\u2500'+' y')
                elif q2 < 0:
                    q2 *= -1
                    print('x      ', (len(s)-q2-3)*'\u2500'+'*'+q2*'\u2500'+'\u253C'+(len(s)-2)*'\u2500'+' y')
            else:
                if f ==0:
                    print('x      ', (len(s)-2)*'\u2500'+'\u253C'+(len(s)-2)*'\u2500'+' y')
                    for j in range(round(first)-1):
                        print((6+len(s))*' '+'\u2502')
                    f = 1
                if q2 > 0:
                    q2 *= -1
                    print('{:0.3f}  '.format(x)+(len(s)-1)*' '+'\u2502'+(q2-1)*' '+'*')
                elif q2 == 0:
                    print('{:0.3f} '.format(x)+len(s)*' '+'*')
                elif q2 < 0:
                    q2 *= -1
                    print('{:0.3f}  '.format(x)+(len(s)-q2-1)*' '+'*'+(q2-1)*' '+'\u2502')
        x = round(x + step, 7)
elif k1 > 0 and k2 < 0:
    print('\nГрафик функции q1 = x^x + 2x - 6: \n')
    m = 27
    s = ((arg//2+1)+m)*'\u0000'
    if max1 > (arg//2+1)+m:
        m = max1
        s = m*'\u0000'
    for i in range(arg):
        q1 = round(copysign(abs(x)**abs(x), x) + 2*x - 6)
        if x < 0:
            if q1 < 0:
                q1 *= -1
                print('{:0.3f} '.format(x)+(len(s)-q1-1)*' '+'*'+(q1-1)*' '+'\u2502')
            elif q1 == 0:
                print('{:0.3f} '.format(x)+(len(s)-1)*' ')
            elif q1 > 0:
                q1 *= -1
                print('{:0.3f} '.format(x)+s+'\u2502'+(len(s)-q1-1)*' '+'*')
        elif x >= 0:
            if x == 0:
                f = 1
                if q1 > 0:
                    q1 *= -1
                    print('x      ', (len(s)-2)*'\u2500'+'\u253C'+(q1-1)+'\u2500'+'*'+(len(s)-2-q1)*'\u2500'+' y')
                elif q1 == 0:
                    print('x      ', (len(s)-2)*'\u2500'+'\u253C'+'*'+(len(s)-2)*'\u2500'+' y')
                elif q1 < 0:
                    q1 *= -1
                    print('x      ', (len(s)-q1-3)*'\u2500'+'*'+q1*'\u2500'+'\u253C'+(len(s)-2)*'\u2500'+' y')
            else:
                if f ==0:
                    print('x      ', (len(s)-2)*'\u2500'+'\u253C'+(len(s)-2)*'\u2500'+' y')
                    for j in range(round(first)):
                        print((6+len(s))*' '+'\u2502')
                    f = 1
                if q1 > 0:
                    q1 *= -1
                    print('{:0.3f}  '.format(x)+(len(s)-1)*' '+'\u2502'+(q1-1)*' '+'*')
                elif q1 == 0:
                    print('{:0.3f} '.format(x)+len(s)*' '+'*')
                elif q1 < 0:
                    q1 *= -1
                    print('{:0.3f}  '.format(x)+(len(s)-q1-1)*' '+'*'+(q1-1)*' '+'\u2502')
        x = round(x + step, 7)
if f == 0:
        for j in range(round(last)*-1):
            print((len(s)+6)*' '+'\u2502')
        print('x      ', (len(s)-2)*'\u2500'+'\u253C'+(len(s)-2)*'\u2500'+' y')
        f = 1
print((6+len(s))*'\u0000'+'x')
