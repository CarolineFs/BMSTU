#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Список специальных символов разделения
special_char = '[@_!#$%^&*()<>?/\|}{~:] ,.\"\'\n\r'


# Функция сдвига символа(char) из алфавита(alphabet) на сдвиг (offset)
def caesar_char(alphabet, char, offset):
    index = alphabet.index(char)
    size_alphabet = alphabet.__len__()
    index = (index + offset) % size_alphabet
    return alphabet[index]


# Функция добавления символа, если специальный символ, то не сдвигается, а просто возвращается то же значение
def append_char(alphabet, char, offset):
    if special_char.__contains__(char):
        return char
    else:
        return caesar_char(alphabet, char, offset)


# Функция сдвига символов(message) из алфавита(alphabet) на сдвиг (offset)
def caesar_string(alphabet, message, offset):
    new_str = ""
    for c in message:
        is_upper = c.isupper()
        c = c.lower()
        new_char = append_char(alphabet, c, offset)
        if is_upper:
            new_str += new_char.upper()
        else:
            new_str += new_char

    return new_str


# Русский алфавит
def ru_alphabet():
    return u"абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


# Английский алфавит алфавит
def en_alphabet():
    return "abcdefghijklmnopqrstuvwxyz"


# Пример шифра Цезаря для русского текста на 3 символа
def example_ru():
    global_alphabet = ru_alphabet()
    string = u"Привет, мир!!?"
    string = caesar_string(global_alphabet, string, 3)
    print(string)


# Пример шифра Цезаря для русского текста на 3 символа
def example_en():
    global_alphabet = en_alphabet()
    string = "Hello, world!!?"
    string = caesar_string(global_alphabet, string, 3)
    print(string)


if __name__ == '__main__':
    example_ru()
    example_en()
