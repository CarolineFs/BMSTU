'''
Написать функцию для формирования строчки из случайных символов и записи в файл

Написать функцию для чтения данных из файла и подсчета количества анаграмм
в файле

Функция для подсчета, сколько раз символ встретился в файле
'''

import random


def writer_random_str_in_file():
    symbols = 'qwertyuiopasdfghjklzxcvbnm' + \
              'йцукенгшщзхъэждлорпавфячсмитьбюё' +\
              '1234567890' +\
              '!@#$%^&*()_+-=№;: '"><,./\[]{}|"
    START = 0
    END = len(symbols) - 1
    random_str = ''
    random_str_len = random.randrange(1, 50, 1)
    for i in range(random_str_len - 1):
        random_str += symbols[random.randrange(START, END, 1)]

    with open('random_str.txt', 'w', encoding='UTF-8') as f:
        f.write(random_str)


def search_anagrams():
    with open('search_anagramms.txt', 'r', encoding='UTF-8') as f:
        text = f.read()
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].strip('!@#$%^&*()_+[]{}'"/.,<>|\№")

    anagrams = 0
    for i in range(len(text)):
        word1 = text[i]
        for j in range(i + 1, len(text)):
            word2 = text[j]
            for l in range(len(word2)):
                if word2[l] in word1:
                    word2.pop(l)
                    word1.pop(word2[l])

        print(text)


search_anagrams()
