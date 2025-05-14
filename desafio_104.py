def leiaInt(k = ' '):
    while True: 
        n = input(k)
        if n.isnumeric():
            print(f'Inteiro {n} lido com sucesso!')
            break
        else:
            print('\033[0:31mErro. Não é um valor numérico inteiro\033[m')



n = leiaInt('Digite um número:')