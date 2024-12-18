from math import factorial
'''
cont = 0
result = 0
fatorial = 0
while cont != 2:
    n1 = int(input('Digite um numero para saber seu fatorial: '))
    fatorial = factorial(n1)
    print(f'O fatorial de {n1}! é {fatorial}!')
    cont = int(input('Digite 1 para continuar e 2 para parar: '))
    if cont == 2:
        print('Fim do programa!')
'''

n1 = int(input('Digite um numero para saber seu fatorial: '))
c = n1
print(f'Calculando {n1}! =', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    c -= 1
print(factorial(n1))