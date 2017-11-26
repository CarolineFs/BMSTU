'''
Назначение:
работа с "базой данных"

Овчинникова Анастасия

Переменные
'''
import pickle
import os

stars = [{'Электра': '372 6'}, {'Меропа': '440 4'},
         {'VY Большого Пса': '3900 1420'}, {'Бетельгейзе': '427 950'},
         {'VV Цефея A': '5000 1050'}, {'UY Щита': '9500 1708'}, {'AH Скорпиона': '7400 1287'},
         {'WOH G64': '163000 1540'},{'KY Лебедя': '5153 1420'},
         {'Альдебаран': '65 43'}, {'Сириус' : '8.6 1.7'},
         {'NML Лебедя': '5300 1183'}, {'Арктур' : '36.7 25.7'}]

with open('data.bin', 'wb') as f:
    pickle._dump(stars, f)

def shower(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            opt_t(flag, FILENAME)
            print()
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
            print()
            print('Название звезды - расстояние от Солнца (св.л.) - солнечных радиусов')
            print()
            for star in stars:
                for key in star.keys():
                    print(key, star[key])
            opt_t(flag, FILENAME)


def adder(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            stars = []
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
    key = input('Введите название звезды: ').strip()
    value = input('Введите расстояние до звезды: ').strip()
    value += ' '
    value += input('Введите радиус звезды (солнечный радиус): ').strip()
    print()
    star = {}
    star[key] = value
    stars.append(star)
    with open(FILENAME, 'wb') as f:
        pickle.dump(stars, f)
    opt_t(flag)


def deleter(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            print()
            opt_t(flag)
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
            opt_t(flag)


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
            all_keys = []
            for star in stars:
                for key in star.keys():
                    all_keys.append(key)
            all_dist = []
            all_rad = []
            for star in stars:
                for i in star.values():
                    i = i.split()
                    d = i[0]
                    r = i[1]
                    all_dist.append(d)
                    all_rad.append(r)
            opt_sr = opt_search(flag, FILENAME)
            if opt_sr == '1':
                pattern = input('Введите название звезды: ').strip()
                for i in range(len(all_keys)):
                    if all_keys[i].lower() == pattern.lower():
                        print()
                        print('Расстояние до этой звезды: '+all_dist[i]+'св.л.')
                        print('Радиус этой звезды: '+all_rad[i])
                        break
                    if i == len(all_keys) - 1:
                        print('Такой звезды нет в каталоге. ')
            elif opt_sr == '2':
                dist = float(input('Введите расстояние до звезды: '))
                st = []
                for i in range(len(all_dist)):
                    if float(all_dist[i]) > dist:
                        st.append(all_keys[i])
                if len(st) == 0:
                    print('В каталоге нет звезд, расстояние до которых больше '+'{:0.4f}'.format(dist)+' св.л.')
                else:
                    print('Звезды, расстояние до которых больше '+'{:0.4f}'.format(dist)+'св.л.')
                    for i in st:
                        print(i)
            elif opt_sr == '3':
                rad = float(input('Введите расстояние до звезды: '))
                st = []
                for i in range(len(all_rad)):
                    if float(all_rad[i]) > rad:
                        st.append(all_keys[i])
                if len(st) == 0:
                    print('В каталоге нет звезд, радиус которых больше '+'{:0.4f}'.format(rad)+' св.л.')
                else:
                    print('Звезды, расстояние до которых больше '+'{:0.4f}'.format(rad)+' св.л.')
                    for i in st:
                        print(i)
            else:
                print('Некорректный ввод. ')
            opt_t(flag, FILENAME)


def sorter(FILENAME, flag):
    with open(FILENAME, 'rb') as file:
        f = file.read()
        if len(f) == 0:
            print()
            print('Здесь ничего нет. ')
            print()
            opt_t(flag, FILENAME)
        else:
            with open(FILENAME, 'rb') as file:
                stars = pickle.load(file)
            print()
            print('Выберите дальнейшее действие:')
            print('1 - сортировка по названию')
            print('2 - сортировка по расстоянию')
            print('3 - сортировка по радиусу')
            opt = input('1/2/3: ')
            if opt == '1':
                print()
                print('Расстояние до некоторых звезд и их радиус')
                letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghigklmnopqrstuvwxyz0123456789'
                for i in letters:
                    for star in stars:
                        for name in star.keys():
                            n = name.lower()
                            if n[0] == i:
                                print(name, star[name])
            else:
                all_dist = []
                all_rad = []
                for star in stars:
                    for i in star.values():
                        i = i.split()
                        d = float(i[0])
                        r = float(i[1])
                        all_dist.append(d)
                        all_rad.append(r)
                print(all_rad, all_dist)
                if opt == '2':
                    print()
                    print('Расстояние до некоторых звезд и их радиус')
                    print()
                    for d in sorted(all_dist):
                        for star in stars:
                            for v in star.values():
                                q = v.split()
                                q = q[0]
                                if float(q) == d:
                                    for k in star.keys():
                                        print(k, v)
                elif opt == '3':
                    print('Расстояние до некоторых звезд и их радиус')
                    print()
                    for r in sorted(all_rad):
                        for star in stars:
                            for v in star.values():
                                q = v.split()
                                q = q[1]
                                if float(q) == r:
                                    for k in star.keys():
                                        print(k, v)
                else:
                    print('Некорректный ввод. ')
        opt_t(flag, FILENAME)

def opt_f(flag):
    print('Выберите действие (для выхода нажмите ENTER): ')
    print('1 - создать новый файл')
    print('2 - работа с существующим файлом')
    opt1 = input('1/2: ')
    if opt1 == '1':
        f = open('new_data.bin', 'wb')
        f.close()
        print()
        print('Создана пустая база данных. ')
        print()
    elif opt1 == '2':
        opt_s(flag)
    elif opt1 == '':
        pass
    else:
        print('Некорректный ввод. ')
        opt_f(flag)


def opt_s(flag):
    print()
    print('Выберите файл для работы (нажмите ENTER, чтобы вернуться назад): ')
    print('1 - ваша база данных')
    print('2 - наша база данных')
    opt2 = input('1/2: ')
    if opt2 == '1':
        if flag:
            FILENAME = 'new_data.bin'
            opt_t(flag, FILENAME)
        else:
            print('Вы еще не создали свою базу данных. ')
            opt_s(flag)
    elif opt2 == '2':
        FILENAME = 'data.bin'
        opt_t(flag, FILENAME)
    elif opt2 == '':
        opt_f(flag)
    else:
        print('Некорректный ввод. ')
        opt_s(flag)


def opt_t(flag, FILENAME):
    print()
    print('Выберите дальнейшее действие (нажмите ENTER, чтобы вернуться назад): ')
    print('1 - просмотр всех записей')
    print('2 - добавление новой записи')
    print('3 - удаление записи')
    print('4 - поиск')
    print('5 - сортировка')
    opt3 = input('1/2/3/4/5: ')
    if opt3 == '1':
        shower(FILENAME, flag)
    elif opt3 == '2':
        adder(FILENAME, flag)
    elif opt3 == '3':
        deleter(FILENAME, flag)
    elif opt3 == '4':
        searcher(FILENAME, flag)
    elif opt3 == '5':
        sorter(FILENAME, flag)
    elif opt3 == '':
        opt_s(flag)
    else:
        print('Некорректный ввод. ')
        opt_t(flag, FILENAME)


def opt_search(flag, FILENAME):
    print()
    print('Выберите тип поиска: ')
    print('1 - поиск по названию звезды')
    print('2 - поиск по расстоянию до звезды')
    print('3 - поиск по радиусу звезды')
    opt_sr = input('1/2/3: ')
    return opt_sr

flag = False
opt_f(flag)

if flag:
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'new_data.bin')
    os.remove(path)
