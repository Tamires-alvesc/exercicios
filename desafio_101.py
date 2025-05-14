from datetime import date #pode ser colocado dentro da função p economizar memoria


def voto(ano):
    idade = date.today().year - ano 
    if idade < 16:
        print(f'{idade} anos. Voto NEGADO') #ou return f'{idade} anos. Voto NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        print(f'{idade} anos. Voto OPCIONAL')
    elif 18 <= idade < 65:
        print(f'{idade} anos. Voto OBRIGATÓRIO')


ano_nasc = int(input('Digite seu ano de nascimento:'))
voto(ano_nasc)
