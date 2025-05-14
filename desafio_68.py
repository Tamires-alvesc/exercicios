from random import randint
soma = 0 
cont = 0

while True:
    pc = randint (0,10)
    pessoa = int(input('Digite o número que você quer:\n'))
    opcao = ' '
    while opcao not in 'PI':
        opcao = str(input('Você quer par ou ímpar? [P/I]\n')).strip().upper()[0]
    soma = pc + pessoa 
    if soma % 2 == 0 and opcao == 'P':
        print(f'Você ganhou do computador. Ele escolheu {pc} e você {pessoa}, logo a soma foi {soma}, que é par.')
        cont += 1
    elif soma % 2 != 0 and opcao == 'I':
        print(f'Você ganhou do computador. Ele escolheu {pc} e você {pessoa}, logo a soma foi {soma}, que é ímpar.')
        cont += 1
    else:
        print(f'Você perdeu para o computador. Ele escolheu {pc} e você {pessoa}, logo a soma foi {soma}. Você ganhou {cont} vez(es) antes de perder.')
        break
    print('Vamos jogar novamente...')



