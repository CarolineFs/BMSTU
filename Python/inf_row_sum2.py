eps = float(input('Введите эпсилон: '))
x = float(input('Введите x: '))
N = int(input('Введите N: '))

s = f = 0
fc = 1
for n in range (N):
     if n > 0:
          fc *= n
     c = ((-1)**n*float(2*fc))*x**(2*n+1)/(4**n*float(fc)**2*(2*n+1))
     s += c
     if abs(c) < eps:
          print('\nСумма равна', '{:9.4e}'.format(s), '\nРяд сошелся за', \
                n + 1, 'итераций. ')
          f = 1
          break
if f == 0:
     print('\nРяд не сошелся за ', N, 'итераций.')
