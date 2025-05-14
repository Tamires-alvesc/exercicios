frase = str(input('Escreva uma frase:\n')).strip().upper()

sem_espacos = frase.replace(' ', '')


k = len(sem_espacos)

n = 0 

palindromo = True

for l in sem_espacos:
    lk = l
    l_k = sem_espacos[-n-1]
    n = n + 1

    if lk != l_k:
        palindromo = False
        break
if palindromo:
    print('É um palíndromo')
else:
    print('Não é um palíndromo') 


#for c in range (0, k):
#    lk = sem_espacos[c]
#    l_k = sem_espacos[-c-1]
#    if lk != l_k:
#        palindromo = False
#        break
#if palindromo:
#    print('É um palíndromo')
#else:
#   print('Não é um palíndromo') 

#for i,l in enumerate(sem_espacos):


#ordem = sem_espacos[0:k]

#contrario = sem_espacos[::-1]


if sem_espacos[0:k] == sem_espacos[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')


