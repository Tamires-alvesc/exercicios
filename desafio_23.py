frase = str(input('Digite uma frase:\n')).lower().strip()

ocorrencias = frase.count('a')

posi1 = frase.find('a')

posif = frase.rfind('a')

print(f'A letra a aparece {ocorrencias} vezes na frase')

print(f'A primeira ocorrência é na posição {posi1+1}')

print(f'A última ocorrência é na posição {posif+1}')