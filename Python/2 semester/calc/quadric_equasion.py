def solve_quadric_equasion(a, b, c):
    if a == 0:
        if b != 0:
            x1 = -c/b
            x2 = None
        else:
            if c == 0:
                x1 = '(-∞; +∞)'
                x2 = None
            else:
                x1 = None
                x2 = None
    else:
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + d**(1/2))/(2*a)
            x2 = (-b - d**(1/2))/(2*a)
        elif d < 0:
            x1 = 'Нет действительных корней'
            x2 = None
        elif d == 0:
            x1 = -b/(2*a)
            x2 = None
    return x1, x2
