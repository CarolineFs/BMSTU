#Построение синусоиды в заданном диапазоне

from math import sin

first = float(input('Введите начальное значение: '))
last = float(input('Введите конечное значение: '))
step = float(input('Введите шаг: '))

x = first
arg = 0
while x < last:
    x += step
    arg += 1
if round(x, 10) > last:
    arg -= 1
maxm = k = 0
x = first
for i in range (arg+1):
    q = sin(x)
    if q < 0:
        k += 1
    if abs(q) > maxm:
            maxm = abs(q)
    x += step
x = first
maxm += 0.1
kf = maxm/30
f1 = f2 = 1

if k == 0:
    f1 = 0
elif k == arg + 1:
    f2 = 0
arr = [-kf*30, -kf*15, 0, kf*15, kf*30]

Oy = 14*'\u2500'
if k != 0 and k != arg + 1:
    print(5*' '+'{:^15.3f}'.format(arr[0])+'{:^15.3f}'.format(arr[1])+\
          '{:^15.0f}'.format(arr[2])+'{:^15.3f}'.format(arr[3])+\
          '{:^15.3f}'.format(arr[4]))
    print(12*' '+'\u2514'+Oy+'\u2534'+Oy+'\u253C'+Oy+'\u2534'+Oy+\
          '\u2518'+'  y')
elif k == 0:
    print(5*' '+'{:^15.0f}'.format(arr[2])+'{:^15.3f}'.format(arr[3])+\
          '{:^15.3f}'.format(arr[4]))
    print(12*' '+'\u2514'+Oy+'\u2534'+Oy+'\u2518'+'  y')
elif k == arg + 1:
    print(5*' '+'{:^15.3f}'.format(arr[0])+'{:^15.3f}'.format(arr[1])+\
          '{:^15.0f}'.format(arr[2]))
    print(12*' '+'\u2514'+Oy+'\u2534'+Oy+'\u2518'+'  y')
x = first
for i in range(arg + 1):
    q = sin(x)
    sp = round(abs(q)//kf)
    
    if q < 0:
        print('{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+\
              (30-sp-1)*' '+'*'+(sp)*' '+f2*'\u2502')
    if q == 0:
         print('{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+\
               30*' '+'*')
    if q > 0:
         print('{:0.3f}'.format(x)+(12-len('{:0.3f}'.format(x)))*' '+\
               f1*(30*' '+'\u2502')+(sp-1)*' '+'*')
    x += step
    round(x, 7)
print(42*' '+f1*f2*'x')
