'''Назначение:
Вычисление таблицы значений функций.
Построение графика одной из функций.

Овчинникова Анастасия

Переменые:
x - значение агрумента, изменяющееся в цикле
step - шаг
first - начальное значение аргумента
last - конечное значение аргумента
k2 - количество отрицательных значений q2
arg - количество шагов step от first до last
max1_p, max2_p, max1_m, max2_m, max3 - максимальные по модулю значения \
функций q1, q2, q3 соответственно
maxx - максимальная длина в символах переменной x
L1, L2, L3, Lx - текущая длина значений функций q1, q2, q3 и переменной \
x соответственно
kf - коэффицент масштабирования
k - модуль последнего значения деления, изображенного на графике 
zn - номер символа на графике относиельно x = 0, где располагается \
значение функции при данном аргументе
i слежебная
q1, q2, q3 - значения функций q1, q2, q3 соответственно 
'''

from math import sqrt, copysign, trunc

first = float(input('Введите начальное значение: '))
last = float(input('Введите конечное значение: '))
step = float(input('Введите шаг: '))

x = first
arg = 0
while round(x, 7) < last:
    x += step
    arg += 1
    if x > last:
        arg -= 1
        break


max1_p  = max2_p = max1_m = max2_m = max3 = k2 = 0

x = first
maxx = 0
for i in range (arg+1):
    q2 = x**3 - x - 1
    if q2 < 0:
        k2 += 1
        if abs(q2) > abs(max2_m):
            max2_m = int(trunc(abs(q2)))
    elif q2 >= 0:
        if q2 > max2_p:
            max2_p = int(trunc(q2))
    q1 = copysign(abs(x)**abs(x), x) + 2*x - 6
    if q1 < 0:
        if abs(q1) > abs(max1_m):
            max1_m = int(trunc(abs(q1)))
    elif q1 >= 0:
        if q1 > max1_p:
            max1_p = int(trunc(q1))
    q3 = sqrt(abs(q1*q2))
    if q3 > max3:
        max3 = int(trunc(q3))
    x += step

for i in range(arg+1):
    if len(str(x)) > maxx:
        maxx = len(str(x))
    x = round(x + step, 7)    

print('\nКоличество отрицательных значений функции q2 =', k2)

maxx+=10
x = first

print('\n')
print(6*' '+'x'+7*' '+'*'+6*' '+'q1'+6*' '+'*'\
      +6*' '+'q2'+6*' '+'*'+6*' '+'q3')
print((14*4)*'*'+4*'*')
for i in range(arg+1):
    q2 = x**3 - x - 1
    q1 = copysign(abs(x)**abs(x), x) + 2*x - 6
    q3 = sqrt(abs(q1*q2))
    x1 = ' '+'{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+' '+'*'
    if len('{:0.3f}'.format(q1))>12:
        q1 = ' '+'{:9.3e}'.format(q1)+(12-len('{:9.3e}'.format(q1)))*' '+' *'
    else:
        q1 = ' '+'{:0.3f}'.format(q1)+(12-len('{:0.3f}'.format(q1)))*' '+' *'
    if len('{:0.3f}'.format(q2))>10:
        q2 = ' '+'{:9.3e}'.format(q2)+(12-len('{:9.3e}'.format(q2)))*' '+' *'
    else:
        q2 = ' '+'{:0.3f}'.format(q2)+(12-len('{:0.3f}'.format(q2)))*' '+' *'
    if len('{:0.3f}'.format(q3))>10:
        q3 = ' '+'{:9.3e}'.format(q3)+(12-len('{:9.3e}'.format(q3)))*' '
    else:
        q3 = ' '+'{:0.3f}'.format(q3)+(12-len('{:0.3f}'.format(q3)))*' '
    print(x1+q1+q2+q3)
    x += step
    round(x,7)

x = first

if max(max2_m, max2_p) > 60:
    kf = (max(max2_m, max2_p))//60 + 1
else: kf = 1
k = str(kf * 60)

print('\nГрафик функции q2 = x^3 - x - 1: \n\n')

if k2 == arg+1:
    print(( maxx-len(k)+1)*' '+'-'+k+58*' '+'-'+str(kf))
    print('x'+maxx*' '+60*'\u2534'+'  y')
    for i in range (arg+1):
        q2 = round(x**3 - x - 1)
        zn = abs(q2)//kf+1
        print(x, (maxx-len(str(x)))*' '+(60-1-zn)*' '+'*')
        x = round(x + step, 7)
        
elif k2 == 0:
    x = first
    print((maxx-len(k)+2)*' '+k+58*' '+str(kf))
    print('x'+maxx*' '+60*'\u2534'+'  y')
    for i in range (arg+1):
        q2 = round(x**3 - x - 1)
        zn = abs(q2)//kf+1
        print(x, (maxx-len(str(x)))*' '+(zn-1)*' '+'*')
        
        x = round(x + step, 7)

else:
    x = first
    print((maxx-len(k)+1)*' '+'-'+k+(59-len(str(kf))-1)*' '+'-'+str(kf)+'0'+\
          str(kf)+(59-len(str(kf)))*' '+k)
    print('x'+maxx*' '+60*'\u2534'+'\u253C'+60*'\u2534'+'  y')
    for i in range (arg+1):
        q2 = round(x**3 - x - 1)
        zn = abs(q2)//kf
    
        if step >= 1:
            if q2 < 0:
                q2 *= -1
                print(x, (maxx-len(str(x)))*' '+(60 - zn-1)*' '+'*'+(zn)*' '+\
                  '\u2502')
            elif q2 == 0:
                print(x, (maxx-len(str(x)))*' '+60*' '+'*')
            elif q2 > 0:
                print(x, (maxx-len(str(x)))*' '+60*' '+'\u2502'+(zn)*' '+'*')
        else:
            if q2 < 0:
                q2 *= -1
                print(x, (maxx-len(str(x))+1)*' '+(60 - zn-1)*' '+'*'+(zn-1)*' '+\
                  '\u2502')
            elif q2 == 0:
                print(x, (maxx-len(str(x)))*' '+60*' '+'*')
            elif q2 > 0:
                print(x, (maxx-len(str(x)))*' '+60*' '+'\u2502'+(zn-1)*' '+'*')
        
        x = round(x + step, 7) 
