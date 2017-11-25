'''
Назначение:
работа с "базой данных"

Овчинникова Анастасия

Переменные
'''
import pickle
import os


def shower(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            print()
            menu(flag)
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
            print()
            print('Расстояние от Солнца до некоторых звезд (св.л.)')
            print()
            for star in stars:
                for key in star.keys():
                    print(key, star[key])
            menu(flag)
        

def adder(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            stars = []
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
                
    key = input('Введите название звезды: ')
    value = input('Введите расстояние: ')
    print()
    star = {}
    star[key] = value
    stars.append(star)
    with open(FILENAME, 'wb') as f:
        pickle.dump(stars, f)
    menu(flag)


def deleter(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            print()
            menu(flag)
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
            pattern = input('Введите название звезды, которую хотите удалить из списка: ')
            pattern = pattern.lstrip()
            pattern = pattern.rstrip()
            all_keys = []
            for star in stars:
                for key in star.keys():
                    all_keys.append(key)
            for i in range(len(all_keys)):
                if all_keys[i].lower() == pattern.lower():
                    stars.pop(i) 
            with open(FILENAME, 'wb') as f:
                pickle.dump(stars, f)
            menu(flag)


def searcher(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            print()
            menu(flag)
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file) 
            print()
            print('Выберите тип поиска: ')
            print('1 - поиск по названию звезды')
            print('2 - поиск по расстоянию до звезды')
            opt = input('1/2: ')
            all_keys = []
            for star in stars:
                for key in star.keys():
                    all_keys.append(key)
            all_values = []
            for star in stars:
                for value in star.values():
                    all_values.append(value)
            if opt == '1':
                pattern = input('Введите название звезды: ')
                for i in range(len(all_keys)):
                    if all_keys[i].lower() == pattern.lower():
                        print('Расстояние до этой звезды равно', all_values[i])
                    if i == len(all_keys) - 1:
                        print('Такой звезды нет в каталоге. ')
            elif opt == '2':
                pattern = float(input('Введите расстояние: '))
                st = []
                for i in range(len(all_values)):
                    if float(all_values[i]) > pattern:
                        st.append(all_keys[i])
                if len(st) == 0:
                    print('В каталоге нет звезд, расстояние до которых больше '+'{:0.4f}'.format(pattern)+' св.л.')
                else:
                    print('Звезды, расстояние до которых больше '+'{:0.4f}'.format(pattern)+'св.л.')
                    for i in st:
                        print(i)
            else:
                print('Некорректный ввод. ')
            menu(flag)
        
    

def sorter(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            print()
            menu(flag)
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
            print()
            print('Выберите дальнейшее действие:')
            print('1 - сортировка по названию звезды')
            print('2 - сортировка по расстоянию до звезды')
            opt = input('1/2: ')
            if opt == '1':
                print()
                print('Расстояние от Солнца до некоторых звезд (св.л.)')
                letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghigklmnopqrstuvwxyz0123456789'
                for i in letters:
                    for star in stars:
                        for name in star.keys():
                            n = name.lower()
                            if n[0] == i:
                                print(name, star[name])
            elif opt == '2':
                print()
                print('Расстояние от Солнца до некоторых звезд (св.л.)')
                all_values = []
                for star in stars:
                    for value in star.values():
                        all_values.append(float(value))
                for value in sorted(all_values):
                    for star in stars:
                        for v in star.values():
                            if float(v) == value:
                                for k in star.keys():
                                    print(k, v)
            else:
                print('Некорректный ввод. ')
            menu(flag)


def menu(flag):
    print()
    print('Выберите действие (для выхода нажмите ENTER): ')
    print('1 - создать новый файл')
    print('2 - работа с существубющим файлом')
    opt = input('1/2: ')
    if opt == '2':
        print('Выберите файл для работы (для выхода нажмите ENTER): ')
        print('1 - ваша база данных')
        print('2 - наша база данных')
        opt_f = input('1/2: ')
        print()
        if opt_f == '1':
            if flag:
                FILENAME = 'new_data.bin'
            else:
                print('Вы еще не создали свою базу данных. ')
                menu(flag)
        elif opt_f == '2':
            FILENAME = 'data.bin'
        elif opt_f == '':
            return
        else:
            print('Некорректный ввод. ')
            menu(flag)
        print('Выберите дальнейшее действие (для выхода нажмите ENTER): ')
        print('1 - просмотр всех записей')
        print('2 - добавление новой записи')
        print('3 - удаление записи')
        print('4 - поиск')
        print('5 - сортировка')
        opt2 = input('1/2/3/4/5: ')
        if opt2 == '1':
            shower(FILENAME, flag)
        elif opt2 == '2':
            adder(FILENAME, flag)
        elif opt2 == '3':
            deleter(FILENAME, flag)
        elif opt2 == '4':
            searcher(FILENAME, flag)
        elif opt2 == '5':
            sorter(FILENAME, flag)
        elif opt2 == '':
            return
        else:
            print('Некорректный ввод. ')
            menu(flag)
    elif opt == '1':
        f = open('new_data.bin', 'wb')
        f.close()
        print()
        print('Создана пустая база данных. ')
        print()
        flag = True
        menu(flag)
    elif opt == '':
        return
    else:
        print('Некорректный ввод. ')
        menu(flag)


flag = False
flag_cont = False
menu(flag)

if flag:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'new_data.bin')
    os.remove(path)
