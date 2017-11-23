print('eeee')

#const
NAME = 'Расстояние от Солнца до некоторых звезд (св.л.)'

stars = ({'17 Тельца (Электра)': '372'}, {'Меропа': '440'},
         {'VY Большого Пса': '3900'}, {'Альфа Ориона (Бетельгейзе)': '427'},
         {'VV Цефея': '5000'}, {'UY Щита': '9500'}, {'AH Скорпиона': '7400'},
         {'WOH G64': '163000'}, {'Бета Персея (Алголь)': '93'},
         {'KY Лебедя': '5153'}, {'Альфа Тельца (Альдебаран)': '65'},
         {'NML Лебедя': '5300'})


def shower(NAME, stars):
    print(NAME)
    print()
    for names in stars:
        for key in names.keys():
            print(key, names[key])


def adder(stars):
    k = input('Введите название звезды: ')
    v = input('Введите расстояние: ')
    print(k, v)
    # name = {}
    # name[key] = value
    # stars.append(name)


def deleter():
    pass


def searcher():
    pass


def sorter():
    pass


def menu(NAME):
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
    elif opt == '1':
        pass
    elif opt == '':
        pass
    else:
        print('Некорректный ввод. ')
        menu()
        if opt2 == '1':
            shower(NAME)
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


adder(stars)
shower(NAME, stars)
