import os
import re

def deleter():
    names = os.listdir()
    for i in range (len(names)):
     if os.path.isfile(names[i]) is True:
        index = names[i].rindex('.')
        names[i] = names[i][0:index]
    return names   

def countnum():
    k = 0
    flag = 0
    name = deleter()
    for i in range (len(name)):
        for j in range (i):
            if name[i] == name [j]:
                flag +=1
                break
        if flag == 0:
            print(name[i])
        flag = 0
        file = re.search('[1-9]', name[i])
        if file != None:
            k += 1
    return k
print ('Всего файлов, в названии которых встретились цифры: ',countnum())
