'''Назначение:
Шифр Виженера

Овчинникова Анастасия

Переменные:
s - входная строка
key - ключ, вводится пользователем
cipher - зашифрованая исходная строка
alphabet - массив с русским алфавитом
kl - длина ключа
ls - длина исходной строки
num - 
caesar_alphabet - генерируемый в функции алфавит, согласно шифру
ind - позиция данного символа исходной строки в массиве с алфавитом
c, L - шифрование данного символа, генерируемое функцией
'''

s = input('Введите строку: ')
key = input('Введите ключ: ')

cipher = ''
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л',\
            'м','н','о','п','р','с','т','у','ф','х','ц','ч','ш',\
            'щ','ъ','ы','ь','э','ю','я']
kl = len(key)
ls = len(s)
key = key.lower()

def get_cipher(i, ind, alphabet, kl, key):
    num = 0
    caesar_alphabet = []
    num = (i)%kl
    num = alphabet.index(key[num])
    caesar_alphabet = alphabet[num:len(alphabet)]+alphabet[0:num]
    c = caesar_alphabet[ind]
    return c

for i in range(ls):
    current = s[i]
    current = current.lower()
    if current in alphabet:
        ind = alphabet.index(current)
        L = get_cipher(i, ind, alphabet, kl, key)
        if s[i].isupper() == True:
            L = L.upper()
        cipher += L
    else:
        cipher += s[i]
print()
print(cipher)
input()
