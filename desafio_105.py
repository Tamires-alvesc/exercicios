def notas(*n, sit=False):
    """
    função notas:
    parâmetro *n são notas no formato (n1,n2,n3...) - notas de cada aluno da turma
    parametro sit (opcional): situação da turma
    retorna um dicionário turma['quantidade', 'maior', 'menor', 'média', 'situação']
    """
    turma = dict()
    c = 0
    s = 0
    maior = menor = n[0]
    for nota in n: 
        if nota > maior:
           maior = nota
        if nota < menor:
            menor = nota
        c += 1
        s += nota
    turma['quantidade'] = c
    turma['maior'] = maior
    turma['menor'] = menor
    turma['média'] = s/c
    if sit == True:
        if turma['média'] <= 5: 
            turma['situação'] = 'Reprovada'
        elif 5 < turma['média'] < 7:
            turma['situação'] = 'Em recuperação'
        else:
            turma['situação'] = 'Aprovada'
    return turma
   
print('-'*20)
turma_1 = notas(1, 5, 7, 9, sit=True)
print(f' O resultado da turma é {turma_1}')
print('-'*20)

print('-'*20)
turma_2 = notas(8, 0, 10, 10, 9, 8, 5)
print(f' O resultado da turma é {turma_2}')
print('-'*20)