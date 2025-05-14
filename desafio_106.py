from time import sleep

c = ('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30m')

def ajuda(funcao):
    título(f'Acessando o manual do comando \'{funcao}\'', 4)
    print(c[6], end = '')
    help(funcao)
    print(c[0], end = '')
    sleep(2)

def título(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('~'*tam)
    print(f'  {msg} ')
    print('~'*tam)
    print(c[0], end = '')
    sleep(1)

while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    f = str(input('Função ou biblioteca:\n'))
    ajuda(f)
    ans = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if ans == 'N':
        print('FIM!')
        break
título('Até logo', 1)



