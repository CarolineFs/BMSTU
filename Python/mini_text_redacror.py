'''
Назначение:
Удаление заданного слова во всем тексте.
Замена одного слова во всем тексте.
Выравнивание текста по запросу.
Нахождение строки с максимальным количеством слов, начинающихся
на заданную букву.

Овчинникова Анастасия

Переменные:
text - массив строк
del_w - слово, которое нужно удалить в тексте, вводится с клавиатуры
rep_w_obj - слово, которое нужно заменить в тексте, вводится с клавиатуры
rep_w_sbj - слово, на которое нужно заменить слово, которое нужно заменить, вводится с клавиатуры
copy - копия текущий строки, создается в цикле
dlt - индекс первого элемента последовательности, которую нужно удалить или заменить
letter - бпрограмма находит строку с максимальным количеством слов, начинающихся
            на letter
al - задает тип выравнивания
mx - мамаксимальное количеством слов, начинающихся на letter
ind - индекс строки с максимальным количеством слов, начинающихся на letter
c_max - количество слов, начинающихся на letter, в текущей строке, считается в цикле
words - массив всех слов текущей строки, все слова в нижнем регистре, знаки препинания удалены
i,j, symbol - служебные
s - текущее предложение
smax - предложение с максимальным количеством слов, начинающихся на заданную букву
'''

def delete_word(text, del_w):
    for i in range(len(text)):
        copy = text[i]
        copy = copy.lower()
        del_w = del_w.lower().strip('.,!?*()«»\'";:-+=[]{}/ ')
        dlt = copy.find(del_w)
        punct = ',.!?:;\'\"()/\[]{}@*& '
        while dlt != -1:
            if copy[dlt-1] in punct or dlt == 0:
                if dlt == len(copy)-len(del_w) or copy[dlt+len(del_w)] in punct:
                    text[i] = text[i][0:dlt]+text[i][dlt+len(del_w):len(text[i])]
            dlt = copy.find(del_w, dlt+len(del_w))
            if dlt == -1:
                break

      
def replace_word(text, rep_w_obj, rep_w_sbj):
    for i in range(len(text)):
        copy = text[i]
        copy = copy.lower()
        rep_w_obj = rep_w_obj.lower().strip('.,!?*()«»\'";:-+=[]{}/ ')
        dlt = copy.find(rep_w_obj)
        while dlt != -1:
            punct = ',.!?:;\'\"()/\[]{}@*& '
            if copy[dlt-1] in punct or dlt == 0:
                if dlt == len(copy)-len(rep_w_obj) or copy[dlt+len(rep_w_obj)] in punct:
                    end = text[i][dlt+len(rep_w_obj):len(text[i])]
                    text[i] = text[i][0:dlt]+rep_w_sbj+end
            dlt = copy.find(rep_w_obj, dlt+len(rep_w_obj))
            if dlt == -1:
                break

def max_letter(text, letter):
    mx = - 1
    ind = -1
    s = ''
    ends = ['.','!','?']
    for t in range(len(text)):
        for symbol in text[t]:
            if symbol not in ends:
                s += symbol
            else:
                s += symbol
                c_max = 0
                words = s.lower().split()
                for j in words:
                    j = j.strip('.,!?*()«»\'";:-+=[]{}/ ')
                    if j.startswith(letter):
                        c_max += 1
                if c_max > mx and c_max != 0:
                    mx = c_max
                    ind = t
                    smax = s
                s = ''
    if ind == -1:
        print('\nВ тексте нет слов, начинающихся на букву "'+letter+'".')
    else:
        print('\nВ предложении "'+smax+'" больше всего слов, начинающихся на букву "'+letter+'"')  

def text_alignment(text, al):
    print()
    print()
    max_len = 0
    for i in text:
        if len(i)>max_len:
            max_len = len(i)
    if al == 'left':
        for i in text:
            print()
            print(i)
    elif al == 'right':
        for i in text:
            print()
            print(' '*(max_len - len(i))+i)
    elif al == 'center':
        for i in text:
            print()
            print(i.center(max_len))
            '''sp = max_len-len(i)
            if sp % 2 == 0:
                print(int((sp/2))*' '+i+int((sp/2))*' ')
            else:
               print(int((sp//2))*' '+i+int(((sp//2)+1))*' ')'''

text = ['Когда взрывается звезда, массивнее Солнца в 4-8 раз, остается ядро с большой плотностью, ', \
'продолжающее разрушаться. Гравитация так сильно давит на материал, что заставляет',\
'протоны и электроны сливаться, чтобы предстать в виде нейтронов. Так и рождается нейтронная',\
'звезда. Эти массивные объекты способны достигать в диаметре всего 20 км. Чтобы',\
' вы осознали плотность, всего одна ложечка такого материала будет весить миллиард тонн. Гравитация',\
' на таком объекте в 2 миллиарда раз сильнее земной, а мощности хватает для гравитационного линзирования, \
позволяющего ученым рассмотреть заднюю часть ','звезды. Толчок от взрыва оставляет импульс, \
который заставляет нейтронную звезду вращаться, достигая нескольких оборотов в секунду.']

print('Исходный текст:\n')
for i in text:
    print(i)

del_w = input('\nВведите слово, которое нужно удалить в тексте: ')
rep_w_obj = input('\nВведите слово, которое нужно заменить: ')
rep_w_sbj= input('Введите слово, на которое нужно заменить: ')
letter = input('\nВведите букву: ')
al = input('\nВведите "left", чтобы выровнять текст по левому краю,\n\
"right" - по правому, или "center", чтобы выровнять текст по центру: ')
letter = letter.lower().strip('.,!?*()«»\'";:-+=[]{}/ ')
al = al.lower().strip('.,!?*()«»\'";:-+=[]{}/ ')

if del_w != '':
    for i in range(len(text)):
        if del_w in text[i].strip('.,!?*()«»\'";:-+=[]{}/ ').split():
            delete_word(text, del_w)
            break
        if i == len(text)-1:
            print('\nВНИМАНИЕ, слова, которое вы просите удалить, нет в тексте. ')
else:
    print('\nВНИМАНИЕ, вы попросили удалить пустое слово. ')

if rep_w_obj != '':
   for i in range(len(text)):
        if rep_w_obj in text[i].strip('.,!?*()«»\'";:-+=[]{}/ ').split():
            replace_word(text, rep_w_obj, rep_w_sbj)
            break
        if i == len(text)-1:
            print('\nВНИМАНИЕ, слова, которое вы просите заменить, нет в тексте. ') 
else:
    print('\nВВНИМАНИЕ, вы попросили заменить пустое слово. ')

if letter != '' and len(letter) == 1:
    max_letter(text, letter)
else:
    if letter == '':
        print('\nВНИМАНИЕ, вы не ввели букву. ')
    elif len(letter) > 1:
        print('\nВНИМАНИЕ, вы ввели не одну букву. ')
        
if al == 'right' or al == 'left' or al == 'center':
    text_alignment(text, al)
else:
    print('\nВВНИМАНИЕ, вы неправильно задали выравнивание. ')
    al = 'left'
    text_alignment(text, al)

input()
