
#aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta

exp = input('Digite uma expressão qualquer que use parênteses:')

pilha = []

for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
