'''
Написать функцию для формирования строчки из случайных символов и записи в файл
Написать функцию для чтения данных из файла и подсчета количества анаграмм
в файле
Функция для подсчета, сколько раз символ встретился в файле
'''

import random

# CONST
FILE_TO_WRITE_RANDOM_STR = 'random_str.txt'
FILE_TO_SEARCH_ANAGRAMS = 'search_anagrams.txt'
FILE_TO_COUNT_SYMBOL = 'count_symbol.txt'
ENCODING = 'UTF - 8'


def writer_random_str_in_file():
    symbols = 'qwertyuiopasdfghjklzxcvbnm' + \
              'йцукенгшщзхъэждлорпавфячсмитьбюё' +\
              '1234567890' +\
              '!@#$%^&*()_+-=№;: \'"><,./\[]{}|'
    start = 0
    end = len(symbols) - 1
    random_str = ''
    random_str_len = random.randrange(1, 50, 1)
    for i in range(random_str_len - 1):
        random_str += symbols[random.randrange(start, end, 1)]

    with open(FILE_TO_WRITE_RANDOM_STR, 'w', encoding=ENCODING) as f:
        f.write(random_str)


def converter_word_into_array(word):
    array = []
    for i in word:
        array.append(i)
    return array


def search_anagrams():
    with open(FILE_TO_SEARCH_ANAGRAMS, 'r', encoding=ENCODING) as f:
        text = f.read()
    text = text.split()
    for i in range(len(text)):
        text[i] = text[i].strip('!@#$%^&*()_+[]{}'"/.,<>|\№")

    anagrams = 0
    for i in range(len(text)):
        word1 = converter_word_into_array(text[i])
        for j in range(i + 1, len(text)):
            word2 = converter_word_into_array(text[j])
            if len(word2) == len(word1):
                for k in text[i]:
                    if k in word2:
                        word2.remove(k)
                        word1.remove(k)
                        if len(word1) == len(word2) == 0:
                            anagrams += 1

    print('Количество анаграмм в файле ' + FILE_TO_SEARCH_ANAGRAMS +
          ' : ' + str(anagrams))


def counter_symbol_in_file():
    with open(FILE_TO_COUNT_SYMBOL, 'r', encoding=ENCODING) as f:
        text = f.read()
    symbol = input('\nВведите символ: ')
    if len(symbol) != 1:
        print('Это не один символ, но я посчитаю,' +
              'сколько раз эта последовательность символов встречается в файле. ')
    k = text.count(symbol)
    if k != 0:
        print('Символ (последователность) "' + symbol +
              '" встречается в файле ' +
              str(k) + ' раз. ')
    else:
        print('Этот символ (последовательность) не встречается в файле. ')


def main():
    writer_random_str_in_file()
    search_anagrams()
    counter_symbol_in_file()


main()
