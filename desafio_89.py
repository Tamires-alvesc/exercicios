#le nome e duas notas, guarda em lista composta
#mostra boletim contendo médiae permite que usuário mostre as notas de cada um individualmente.
lista = []
cont = 0

while True:
    aluno = []
    nome = str(input('Qual o nome?\n'))
    n1 = float(input('Digite a nota 1:\n'))
    n2 = float(input('Digite a nota 2:\n'))
    media = (n1 + n2)/2
    aluno = [nome, [n1, n2], media]
    lista.append(aluno[:])
    cont += 1
    ans = str(input('Deseja continuar cadastrando? [S/N]')).upper().strip()[0]
    if ans == 'N':
        break

print('Segue o boletim com as médias de cada aluno:')
print('Aluno.....................Média')
for c in range(0, cont):
    print(f'{lista[c][0]}.....................{lista[c][2]}')

while True:
    escolha = int(input('De qual aluno quer saber as notas? (999 interrompe) \n'))
    if escolha == 999:
        break
    if escolha <= len(lista) - 1:
        print(f'As notas de {lista[escolha-1][0]} foram {lista[escolha-1][1]} ')
    

#print('-='*30)
#print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
#print('-'*26)
# for i, a in enumerate(lista):
#   print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')