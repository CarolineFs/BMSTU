'''Назначение:
определение для одномерного массива, что больше: среднее
арифметическое положиьельных элементов с четными индексами
или среднее арифметическое элементов, у которых индексы
кратны трем.

Овчинникова Анастасия

Переменные:
arr - массив, вводимый пользователем
numbers - массив с цифрами
s2 - сумма положительных элементов с четными индексами
s3 - сумма элементов, у которых индексы кратны 3
k2 - количество элементов с четными индексами
k3 - количество элементов, у которых индексы кратны 3
i, j, f, ef - служебные
'''

arr = []
f = 0
ef = 0
s2 = s3 = 0
k2 = k3 = 0
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
     arr = input('Введите элементы массива через пробел: ').split()
     f == 0
     for i in range(len(arr)):
          for j in range(len(arr[i])):
               '''if j ==0 and arr[i][j]  == '-':
                    f = 0
               if j != 0 and j != len(arr[i])-2 and \
               (arr[i][j] == '.' or arr[i][j] =='e'):
                    f = 0'''
               if ef == 0:
                    if j != 0 and j != len(arr[i])-2 and \
                       arr[i][j] =='e' and arr[i][j+1] == '-':
                         ef = 1
               if ef == 1:
                    ef = 2
               if (j != 0 and j != len(arr[i])-2 and (arr[i][j] != '.' or\
                    arr[i][j] != 'e') and ef == 0) or \
                  (j == 0 and arr[i][j] != '-' and ef == 0):
                    if arr[i][j] not in numbers:
                         f = 1
                         ef = 0
                         print('Неверный формат, попробуйте снова.')
                         break
               if j == len(str(arr[i]))-1:
                    arr[i] = float(arr[i])
                    f = 0
          if f == 1:
               break
     if f == 0:
          break
     
for i in range(len(arr)):
     if i % 2 == 0 and arr[i] > 0:
          s2 += arr[i]
          k2 += 1
     elif i % 3 == 0:
          s3 += arr[i]
          k3 += 1
if k2 != 0:
    s2 = s2/k2
else: s2 = 0
if k3 != 0:
     s3 = s3/k3
else: s3 = 0
if s2 > s3:
     print('\nСреднее арифметическое элементов с четными индексами \
больше, чем среднее арифметическое элементов с индексами, кратными 3.')
elif s2 < s3:
     print('\nСреднее арифметическое элементов с индексами, \
кратными 3, больше, чем среднее арифметическое элементов с четными индексами.')
else:
     print('\nСреднее арифметическое элементов с четными \
индексами и среднее арифметическое с индексами, кратными 3, равны.')
          

