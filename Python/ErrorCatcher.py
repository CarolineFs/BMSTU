def CatchIntError(c):
    if c.isdigit():
        c = int(c)
    return c

def CatchFloatError(c):
    if c.isdigit():
        return float(c)
    else:
        n = ''
        nums = '0123456789-'
        for i in range(len(c)):
            if i != 0 and i != len(c) - 1 and c[i] in '0123456789':
                n += c[i]
            elif i == 0 and c[i] in nums:
                if c[i] == '-' and len(c) != 1:
                    n += c[i]
                else:
                    break
            elif i == len(c)-1 and i != 0 and (c[i] in nums[0:10] or c[i] == '.'):
                n += c[i]
            elif i != 0 and i != len(c)-1 and c[i] == '.':
                if '.' not in n and 'e' not in n:
                    n += c[i]
            elif i != 0 and i != len(c)-1 and c[i] == '-':
                if c[i-1] == 'e':
                    n += c[i]
            elif i != 0 and i != len(c)-1 and c[i] == 'e':
                if 'e' not in n:
                    n += c[i]
            else:
                break
        if len(n) == len(c) and len(n) != 0:
            n = float(n)
        return n
