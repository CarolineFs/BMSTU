'''Назначение:
Вычисление таблицы значений функций.
Построение графика одной из функций.

Овчинникова Анастасия

Переменые:
x - значение агрумента, изменяющееся в цикле
step - шаг
first - начальное значение аргумента
last - конечное значение аргумента
k2 - количество отрbцательных значений q2
arg - количество шагов step от first до last
max2_p, max2_m - максимальные по модулю значения функций \
q1, q2, q3 соответственно
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

from math import sqrt, copysign, ceil

first = float(input('Введите начальное значение: '))
last = float(input('Введите конечное значение: '))
step = float(input('Введите шаг: '))

x = first
arg = 0

while x < last:
    x += step
    arg += 1

if round(x, 7) > last:
    arg -= 1


max1_p  = max2_p = max1_m = max2_m = max3 = k2 = maxx = 0
x = first

for i in range (arg+1):
    q2 = x**3 - x - 1
    if q2 < 0:
        k2 += 1
        if abs(q2) > abs(max2_m):
            max2_m = abs(q2)
    elif q2 >= 0:
        if q2 > max2_p:
            max2_p = q2
    q1 = copysign(abs(x)**abs(x), x) + 2*x - 6
    q3 = sqrt(abs(q1*q2))

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
m = max(max2_p, max2_m)+1
kf = round(m/30,1)
f1 = f2 = 1
if k2 == 0:
    f1 = 0
elif k2 == arg + 1:
    f2 = 0

print('\nГрафик функции q2 = x^3 - x - 1: \n\n')

arr = [-kf*30, -kf*15, 0, kf*15, kf*30]
Oy = 14*'\u2500'
if k2 != 0 and k2 != arg + 1:
    print(5*' '+'{:^15.3f}'.format(arr[0])+'{:^15.3f}'.format(arr[1])+\
          '{:^15.0f}'.format(arr[2])+'{:^15.3f}'.format(arr[3])+\
          '{:^15.3f}'.format(arr[4]))
    print(12*' '+'\u2514'+Oy+'\u2534'+Oy+'\u253C'+Oy+'\u2534'+Oy+\
          '\u2518'+'  y')
elif k2 == 0:
    print(5*' '+'{:^15.0f}'.format(arr[2])+'{:^15.3f}'.format(arr[3])+\
          '{:^15.3f}'.format(arr[4]))
    print(12*' '+'\u2514'+Oy+'\u2534'+Oy+'\u2518'+'  y')
elif k2 == arg + 1:
    print(5*' '+'{:^15.3f}'.format(arr[0])+'{:^15.3f}'.format(arr[1])+\
          '{:^15.0f}'.format(arr[2]))
    print(12*' '+'\u2514'+Oy+'\u2534'+Oy+'\u2518'+'  y')


for i in range(arg + 1):
    q2 = x**3 - x - 1
    sp = round(abs(q2)//kf)
    
    if q2 < 0:
        print('{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+\
              (30-sp-1)*' '+'*'+(sp)*' '+f2*'\u2502')
    if q2 == 0:
         print('{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+\
               30*' '+'*')
    if q2 > 0:
         print('{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+\
               f1*(30*' '+'\u2502')+(sp-1)*' '+'*')

    x += step
    round(x, 7)
print(42*' '+f1*f2*'x')
    

