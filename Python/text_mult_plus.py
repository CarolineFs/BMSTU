text = ['Один два три 8+7. Четыре пять', 'шесть. Семь -0.12*1e-2 восемь', 'девять 4*0', 'одиннадцать! Двенадцать 7.3+0.3 пять', 'шесть 1e3*-3.3 два?']


def printer(text):
    print()
    for i in text:
        print(i)
    print()


def main(text):
    punct = 'e*+.-'
    nums = '0123456789'
    s = ''
    ind = -1
    l = -1
    for st in range(len(text)):
        for i in range(len(text[st])):
            if text[st][i] not in nums and text[st][i] not in punct:
                if s != '':
                    s = s.lstrip('.,/!\|;:@')
                    s = s.rstrip('.,/!\|;:@')
                    if s != '':
                        l= len(s)
                        finder(s, l, ind, st)
                        s = ''
                        ind = -1
                        l = -1
            else:
                if ind == -1:
                    ind = i
                s += text[st][i]
        

def changer(text, res, ind, l, st):
    print(text[st])


def finder(s, l, ind, st):
    if s[0] not in '-1234567890':
        s = s[1:len(s)]
        l -= 1
    nums = s.split('+')
    if len(nums) == 1:
        nums = s.split('*')
    if len(nums) < 2:
        return
    for n in nums:
        if n[0] not in '-1234567890':
            return
        if n[len(n)-1] not in '0123456789.':
            return
        else:
            if 'e' in n:
                if n.count('e') > 1:
                    return
            if '.' in n:
                if n.count('.') > 1:
                    return
            if '-' in n:
                if n.count('-') > 2:
                    return
                elif n.count('-') == 2:
                    if n[n.find('-', 1)-1] != 'e':
                        return
    res = 1
    for n in range(len(nums)):
        nums[n] = float(nums[n])
        res *= nums[n]
    changer(text, res, ind, l, st)
    
    



                
   
        
    

print('Исходный текст. ')
printer(text)


main(text)


printer(text)
