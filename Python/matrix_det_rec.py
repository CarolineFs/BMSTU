
'''Назначение:
вычисление определителя матрицы методом Крамера.

Овчинникова Анастасия

Переменные:
N - порядок матрицы
mtrx - матрица
det - детерминант матрицы
i, j, t, a, b, x, y - служебные
flag - флаговая'''

flag = True
N = int(input('Введите порядок квадратной матрицы: '))

if N <= 0:
     flag = False

if flag:     
     t = j = f = 0
     mtrx = [[0] * (N) for i in range(N)]
     for i in range(N*N):
          mtrx[t][j] = input(('Введите элемент ['+str(t)+'] ['+str(j)+']: '))
          j += 1
          if j == N:
               t += 1
               j = 0

if flag:
     for i in range(len(mtrx)):
          for j in range(len(mtrx[i])):
               if mtrx[i][j] == '' or mtrx[i][j] == ' ':
                    flag = False
                    break
               if  mtrx[i][j].isdigit() == True:
                   mtrx[i][j] = float(mtrx[i][j])
               if type(mtrx[i][j]) is str:
                    if '-' in mtrx[i][j] and '.' not in mtrx[i][j]:
                         if mtrx[i][j].count('-') == 1:
                              if mtrx[i][j].find('-') == 0 and mtrx[i][j][1:len(mtrx[i][j])].isdigit() == True:
                                   mtrx[i][j] = float(mtrx[i][j])
                    elif '.' in mtrx[i][j] and '-' not in mtrx[i][j]:
                         if mtrx[i][j].count('.') == 1:
                              ch = mtrx[i][j].find('.')
                              if ch != 0 and ch != len(mtrx[i][j])-1:
                                   stt = mtrx[i][j][0:ch]+mtrx[i][j][ch+1:len(mtrx[i][j])]
                                   if stt.isdigit() == True:
                                        mtrx[i][j] = float(mtrx[i][j])
                    elif '.' in mtrx[i][j] and '-' in mtrx[i][j]:
                         if mtrx[i][j].count('.') == 1 and mtrx[i][j].count('-') == 1:
                              if mtrx[i][j].find('-') == 0:
                                   ch = mtrx[i][j].find('.')
                              if ch != 0 and ch != len(mtrx[i][j])-1:
                                   stt = mtrx[i][j][1:ch]+mtrx[i][j][ch+1:len(mtrx[i][j])]
                                   if stt.isdigit() == True:
                                        mtrx[i][j] = float(mtrx[i][j])
                                        
               if type(mtrx[i][j]) is str:
                   flag = False
                   break
              
def matrix_determinant(a):
     if len(a) == 1:
          det = a[0][0]
     else:
          b = [[0] * (len(a)-1) for i in range(len(a)-1)]
          det = 0
          for t in range(len(a)):
               x = 0
               y = 0
               for i in range(1,len(a)):
                    for j in range(len(a)):
                         if j != t:
                              b[x][y] = a[i][j]
                              y += 1
                         if y == len(a)-1:
                              x += 1
                              y = 0
               k = matrix_determinant(b)
               det += ((-1)**(t))*a[0][t]*k
     return(det)
if flag:
     print('\ndet =','{:.4f}'.format(matrix_determinant(mtrx)))
else:
     print('\nНекорректные входные данные. ')

