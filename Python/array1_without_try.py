'''Назначение:
Вычисление суммы положительных элементов массива, расположенных на позициях
с четными индексами. Сумма записывается вместо третьего отрицательного элемента.
Если в массиве нет трех отрицательных элементов, то выводится сообщение об этом.

Овчинникова Анастасия

Переменные:
arr - вводимый пользователем массив
numbers - массив с числами
s - сумма положительных элементов массива, расположенных на позициях
с четными индексами
k - количество отрицательных элементов
i, j, ind, ef, f - служебные
'''

arr = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
f = 0
s = 0
k = 0
ef = 0
ind = -1
while True:
     arr = input('Input array all in one string: ').split()
     f == 0
     for i in range(len(arr)):
          for j in range(len(arr[i])):
               '''if j ==0 and arr[i][j]  == '-':
                    f = 0
               if j != 0 and j != len(arr[i])-2 and (arr[i][j] == '.' or\
                                                     arr[i][j] =='e'):
                    f = 0'''
               if ef == 0:
                    if j != 0 and j != len(arr[i])-2 and arr[i][j] =='e' \
                       and arr[i][j+1] == '-':
                         ef = 1
               if ef == 1:
                    ef = 2
               if (j != 0 and j != len(arr[i])-2 and (arr[i][j] != '.' or \
                                                      arr[i][j] != 'e') \
                   and ef == 0) or \
                  (j == 0 and arr[i][j] != '-' and ef == 0):
                    if arr[i][j] not in numbers:
                         f = 1
                         ef = 0
                         print('Incorrect format, try again.')
                         break
               if j == len(str(arr[i]))-1:
                    arr[i] = float(arr[i])
                    f = 0
          if f == 1:
               break
     if f == 0:
          break
if f == 0:
     for i in range(len(arr)):
          if arr[i] < 0:
               k += 1
               if k == 3:
                    ind = i
          if i % 2 == 0:
               if arr[i] > 0:
                    s += arr[i]
     print('The sum of the positive elements of the array:', \
           '{:0.4f}'.format(s))
     if k >= 3:
          arr[ind] = s
          print(arr)
     else:
          print('There are no 3 negative elements in the array.')
