'''
Назначение:
работа с "базой данных"

Овчинникова Анастасия

Переменные
'''
import pickle


def shower():
    with open('data.bin', 'rb') as file:
        stars = pickle.load(file)
    print()
    print('Расстояние от Солнца до некоторых звезд (св.л.)')
    print()
    for star in stars:
        for key in star.keys():
            print(key, star[key])
    menu()
    

def adder():
    with open('data.bin', 'rb') as file:
        stars = pickle.load(file)
    key = input('Введите название звезды: ')
    value = input('Введите расстояние: ')
    print()
    stars[key] = value
    with open('data.bin', 'wb') as f:
        pickle.dump(stars, f)
    menu()


def deleter():
    with open('data.bin', 'rb') as file:
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
            stars = stars.pop(i)
    with open('data.bin', 'wb') as f:
        pickle.dump(stars, f)
    menu()


def searcher():
    with open('data.bin', 'rb') as file:
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
    elif opt == '2':
        pattern = float(input('Введите расстояние: '))
        st = []
        for i in range(len(all_values)):
            if float(all_values[i]) > pattern:
                st.append(all_keys[i])
        if len(st) == 0:
            print('В каталоге нет звезд, расстояние до которых больше '+'{:0.4f}'.format(pattern)+'св.л.')
        else:
            print('Звезды, расстояние до которых больше '+'{:0.4f}'.format(pattern)+'св.л.')
            for i in st:
                print(i)
    else:
        print('Некорректный ввод. ')
        menu()
    menu()
    
    

def sorter():
    print()
    print('Выберите дальнейшее действие:')
    print('1 - сортировка по названию')
    print('2 - сортировка по расстоянию')
    opt = input('1/2: ')
    if opt == '1':
        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghigklmnopqrstuvwxyz0123456789'
        for i in letters:
            for star in stars:
                for name in star.keys():
                    n = name.lower()
                    if n[0] == i:
                        print(name, star[name])
    elif opt == '2':
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
    menu()


def menu():
    print()
    print('Выберите действие (для выхода нажмите ENTER): ')
    print('1 - создать новый файл')
    print('2 - работа с существубющим файлом')
    opt = input('Введите 1 ил 2: ')
    if opt == '2':
        print()
        print('Выберите дальнейшее действие (для выхода нажмите ENTER): ')
        print('1 - просмотр всех записей')
        print('2 - добавление новой записи')
        print('3 - удаление записи')
        print('4 - поиск')
        print('5 - сортировка')
        opt2 = input('1/2/3/4/5: ')
        if opt2 == '1':
            shower()
        elif opt2 == '2':
            adder()
        elif opt2 == '3':
            deleter()
        elif opt2 == '4':
            searcher()
        elif opt2 == '5':
            sorter()
        else:
            print('Некорректный ввод. ')
            menu()
    elif opt == '1':
        pass
    elif opt == '':
        pass
    else:
        print('Некорректный ввод. ')
        menu()

menu()
