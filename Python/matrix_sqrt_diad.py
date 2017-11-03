'''Программа ищет полные квадраты на побочной диагонали. 
Ищет плохо.
'''

from math import sqrt

N = int(input('Введите порядок квадратной матрицы: '))
t = j = f = 0
mtrx = [[0] * (N) for i in range(N)]
for i in range(N*N):
    mtrx[t][j] = float(input(('Введите элемент ['+str(t)+'] ['+str(j)+']: ')))
    j += 1
    if j == N:
        t += 1
        j = 0
f = 0
for i in range(N):
    for j in range(N):
        if i+j == N-1:
            if round(sqrt(mtrx[i][j]),30)*round(sqrt(mtrx[i][j]),10)== mtrx[i][j]:
                if f == 0:
                    print('\nПолные квадраты на побочной диагонали: \n')
                    f = 1
                print(mtrx[i][j])
if f == 0:
    print('\nНа побочной диагонали нет полных квадратов. ')
