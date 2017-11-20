text = ['Eins zwei. Drei', 'vier, sieben acht', 'achtundzwanzig! Siebzehn,', 'dreihunderteinsundvierzig: erste dritte zwolf', 'elf zwolf neun.']

print('Исходный текст: ')
for i in text:
    print(i)

wh = ''
for i in range(len(text)):
    wh += text[i]
    if i != len(text) - 1:
        wh += ' '

text = ['']
j = 0
for i in range(len(wh)):
    text[j] += wh[i]
    if wh[i] in '.!?' and i != len(wh) - 1:
        text.append('')
        j += 1

s = ''
for i in range(len(text)):
    text[i] = text[i].rstrip(' ')
    text[i] = text[i].lstrip(' ')
    if len(text[i]) > len(s):
        s = text[i]

print()
print()
print('Самое длинное предложение: ')
print(s)

words = s.strip(',./?!@#$%^:;"\'[]{}()-_=+*<>').split()

L = len(words[0])

for i in words:
    if len(i) < L:
        L = len(i)

print()
print()
print('Самое короткое слово(слова): ')

for i in words:
    if len(i) == L:
        print(i)

    
    
