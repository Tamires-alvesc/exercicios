from time import sleep

def contador(i, f, p):
    n = i
      
    if i < f and p > 0:
        print(f' {n}', end = '', flush = True)
        while n + p <= f:
            n = n + p 
            sleep(0.5)
            print(f' {n}', end = '', flush = True)
    elif i > f and p > 0:
        print(f' {n}', end = '', flush = True)
        while n - p <= f:
            n = n - p 
            sleep(0.5)
            print(f' {n}', end = '', flush = True)
    elif i > f and p < 0:
        print(f' {n}', end = '', flush = True)
        while n + p >= f:
            n = n + p 
            sleep(0.5)
            print(f' {n}', end = '', flush = True)  
    elif i > f and p == 0:
        print(f' {n}', end = '', flush = True)
        while n - 1 >= f:
            n = n - 1 
            sleep(0.5)
            print(f' {n}', end = '', flush = True)  
    elif i < f and p == 0:
        print(f' {n}', end = '', flush = True)
        while n + 1 >= f:
            n = n + 1
            sleep(0.5)
            print(f' {n}', end = '', flush = True)  
    else:
        print('Erro! Redefina os parâmetros.')
        
          
print('Contagem de 1 a 10, passo 1:')
contador(1, 10, 1)
print('\n')
print('Contagem de 10 a 0, passo -2:')
contador(10, 0, -2)
print('\n')
print('Contagem personalizada:')

i = int(input('Número de início:'))

f = int(input('Número de fim:'))

p = int(input('Passo:'))


contador(i, f, p)
