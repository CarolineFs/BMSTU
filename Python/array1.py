'''Назначение:
Вычисление суммы положительных элементов массива, расположенных на позирциях
с четными индексами. Сумма записывается вместо третьего отрицательного элемента.
Если в массиве нет трех отрицательных элементов, то выводится сообщение об этом.

Овчинникова Анастасия

Переменные:
arr - вводимый пользователем массив
s - сумма положительных элементов с четными индексами
k - количество отрицательных элементов массива
f, i, ind - служебные
'''

arr = []
f = 0
s = 0
k = 0
ind = -1
arr = input('Input array all in one string: ').split()
for i in range(len(arr)):
     try:
          arr[i] = float(arr[i])
     except ValueError:
          print('Incorrect format. ')
          f = 1
          break
if f == 0 and len(arr) != 0:
     for i in range(len(arr)):
          if arr[i] < 0:
               k += 1
               if k == 3:
                    ind = i
          if i % 2 == 0:
               if arr[i] >= 0:
                    s += arr[i]
     if k != len(arr):
         print('The sum of the positive elements of the array:', s)
     if k >= 3 and k != len(arr):
          arr[ind] = s
          print(arr)
     else:
          if k == len(arr):
               print('There are no positive elements in the array.')
          elif k < 3:
                print('There are less than 3 negative elements in the array.')
if len(arr) == 0:
     print('No elements.')
     
