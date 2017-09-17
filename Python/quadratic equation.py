''' Назначение:
решение квадратных уравнений. '''

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

if a == 0:
    if b != 0:
        x = round(-c/b)
        print ('\nx = ', x)
    elif b == 0 and c == 0:
        print ('\nx ∈ (-∞; +∞)')
    elif b == 0 and c != 0:
        print ('\nРешений нет.')
elif a != 0:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b+D**(1/2))/(2*a)
        x2 = (-b-D**(1/2))/(2*a)
        print ('\nx1 = ', x1)
        print ('x2 = ', x2)
    elif D < 0:
        print ('\nРешений нет.')
    elif D == 0:
        x = (-b+D**(1/2))/(2*a)
        print ('\nx = ', x)
