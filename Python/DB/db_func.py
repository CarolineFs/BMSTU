'''
Назначение:
Работа с "базой данных"

Овчинникова Анастасия

Переменные:

'''

import re


def openDB():
    with open('stars.bin', 'r', encoding = 'utf - 8') as f:
        text = f.read()
    return text


def openNewDB():
    with open('nwe_db.txt', 'w', encoding = 'utf - 8') as f:
        pass


def view():
    print()
    print()
    print(openDB())
    


def add():
    new_inf = []
    '''print()
    print('ведите информацию, которую хотите добавить в файл: ')
    print()
    while True:
        s = input()
        new_inf.append(s)
        if s == '':
            break
    with open('stars.txt', 'a', encoding = 'utf - 8') as f:
        for i in new_inf:
            f.writelines(i+'\n')'''
    
    form = ['Название звезды: ', 'Тип: ', 'Расстояние: ', 'Созвездие:',\
               'Масса: ', 'Радиус: ', 'Светимость: ']
    print()
    f = open('stars.txt', 'a', encoding = 'utf - 8')
    f.writelines('\n\n')
    for i in range(len(form)):
        s = input(form[i])
        if i == 0:
            f.writelines(s+'\n')
        else:
            f.writelines('\t'+form[i]+s+'\n')                    
    
    
def search(s, opt):
    with open('stars.bin', 'r', encoding = 'utf - 8') as f:
        text = f.read()
    #Без RegExp
    '''strings = text.split('\n')
    pt = 'Звезды в созвездии '+s+':'
    if opt == '2':
        pt = 'Звезды, расстояние до которых равно '+s+' св.л.:'
        s = 'Расстояние: '+s
    stars = []
    st = []
    for string in strings:
        if string == '':
            for elem in st:
                if s in elem:
                    stars.append(st[0])
                    break
            st = []
        else:
            st.append(string)
    if len(stars) == 0:
        print()
        print('Нет элементов, удовлетворяющих условиям поиска. ')
    else:
        print()
        print(pt)
        for i in stars:
            print(i)'''
    #RegExp
    star_name = '(.+)\n\tТип'
    constel_name = 'Созвездие: (.+)\n'
    stars = re.findall(star_name, text)
    constels = re.findall(constel_name, text)
    print(stars)
    print(constels)
        

def sorting():
    pass


def delete():
    pass


def menu():
    print('Работа с базой данных "Звезды и их физические характеристики"')
    print()
    print('Выберите действие: ')
    print('1 - создать новый файл')
    print('2 - работу с существующим файлом')
    opt1 = input('Введите 1 или 2: ')
    if opt1 == '1':
        openNewDB()
    elif opt1 == '2':
        print()
        print('Выберите дальнейшее действие: ')
        print('1 - просмотр всех записей')
        print('2 - добавление новой запии')
        print('3 - поиск')
        print('4 - сортировка')
        print('5 - удаление')
        opt2 = input('Введите 1, 2, 3, 4 или 5: ')
        if opt2 == '1':
            view()
        elif opt2 == '2':
            add()
        elif opt2 == '3':
            print()
            print('Выберите тип поиска: ')
            print('1 - поиск звезд по созвездиям')
            print('2 - поиск звезд по расстоянию от Солнца')
            opt_search = input('Введите 1 или 2: ')
            if opt_search == '1':
                constel = input('Введите навание созвездия: ')
                search(constel, opt_search)
            elif opt_search == '2':
                dist = input('Введите расстояние от Солнца: ')
                search(dist, opt_search)
        elif opt2 == '4':
            sorting()
        elif opt2 -- '5':
            delete()

menu()
    
