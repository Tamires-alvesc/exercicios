
def fatorial(n, show = False):
    fat = 1
    for c in range(n, 0, -1):
        fat = fat*c
    if show == True:
        for c in range(n,0,-1):
            if c == 1:
                print(f' {c}', end = '')
            else:
                print(f' {c} x', end = '')            
        print(f' = {fat}')
    else:
        print(f'\n O resultado é {fat}')
    


fatorial(4,show = True)

fatorial(5)
