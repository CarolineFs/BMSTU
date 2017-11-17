import os
import shutil
import re
names = os.listdir()
k = 0
flag = 0       
for i in range (len(names)):
    for j in range (i):
        if names[i] == names [j]:
            flag +=1
            break
    if flag == 0:
        print(names[i])
    flag = 0
    file = re.search('[1-9]', names[i])
    if file != None:
        k += 1
print ('Всего файлов, в названии которых встретились цифры: ', k)
