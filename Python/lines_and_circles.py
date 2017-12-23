'''Дано множество точек, координаты центров окружностей и их радиусы.
Найти прямую, проходящую через две из заданных точек такую, чтобы она пересекала (не касалась) 
наибольшее количество окружностей.
'''

from math import sqrt

coords = []

Nc = int(input('Введите количество точек: '))
for i in range(Nc):
    x = float(input('\nВведите x: '))
    y = float(input('Введите y: '))
    arr = [x, y]
    coords.append(arr)

coords_cent = []
rad = []
No = int(input('\nВведите количество окружностей: '))
for i in range(No):
    r = float(input('\nВведите радиус окружности: '))
    x = float(input('Введите x (центр окружности): '))
    y = float(input('Введите y (центр окружности): '))
    arr = [x, y]
    coords_cent.append(arr)
    rad.append(r)

print('\nТочки: ')
print(coords)
print('\nЦентры: ')
print(coords_cent)
print('\nРадиусы: ')
print(rad)

from itertools import combinations
lines = list(combinations(coords, 2))


for i in range(len(lines)):
    x1 = lines[i][0][0]
    y1 = lines[i][0][0]
    x2 = lines[i][1][0]
    y2 = lines[i][1][1]
    if x1 - x1 != 0:
        k = (y1 - y2)/(x1 - x2)
    else:
        k = 0
    b = y2 - k*x2
    max_points = -1
    min_line = []
    f = 0
    points = 0
    for j in range(len(rad)):
        r = rad[j]
        x = coords_cent[j][0]
        y = coords_cent[j][1]
        d = (pow((2*k*b-2*x-2*y*k),2)-(4+4*k*k)*(b*b-r*r+x*x+y*y-2*y*b))  
        if d < 0:
            continue
        else:   
            x3=((-(2*k*b-2*x-2*y*k)-sqrt(d))/(2+2*k*k))   
            x4=((-(2*k*b-2*x-2*y*k)+sqrt(d))/(2+2*k*k))        
            if x3 == x4:
                continue
            else:
                points += 1
    if not f:
        min_points = points
        min_line = lines[i]
    else:
        if min_points < points:
            min_points = points
            min_line = lines[i]

if len(min_line) != 0:
    print('\nОтвет: ')
    print(min_line)
else:
    print('Такой прямой нет. ')


    




