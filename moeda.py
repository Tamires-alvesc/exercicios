
def aumentar(n, k, p = False):
    resultado = n*(1+ k/100)
    if p:
        return moeda(resultado)
    else:
        return resultado



def diminuir(n, k, p = False):
    resultado = n*(1 - k/100)
    if p:
        return moeda(resultado)
    else:
        return resultado


def dobro(n, p = False):
    resultado = n*2
    if p:
        return moeda(resultado)
    else:
        return resultado


def metade(n, p = False):
    resultado = n/2
    if p:
        return moeda(resultado)
    else:
        return resultado


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n, k , z):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço:    {metade(n,True)}')
    print(f'{k}% de aumento:     {aumentar(n,k,True)}')
    print(f'{z}% de aumento:     {aumentar(n,z,True)}')
    print('-'*30)
