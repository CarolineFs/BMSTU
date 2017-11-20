'''
Назначение:
Работа с "базой данных"

Овчинникова Анастасия

Переменные:

'''

import re


def openDB():
    with open('stars.txt', 'r', encoding = 'utf - 8') as f:
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
    print()
    print('ведите информацию, которую хотите добавить в файл: ')
    print()
    while True:
        s = input()
        new_inf.append(s)
        if s == '':
            break
    with open('stars.txt', 'a', encoding = 'utf - 8') as f:
        for i in new_inf:
            f.writelines(i+'\n')
        
    


def search():
    pass


def sorting():
    pass


def delete():
    pass


def menu():
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
            search()
        elif opt2 == '4':
            sorting()
        elif opt2 -- '5':
            delete()

menu()
