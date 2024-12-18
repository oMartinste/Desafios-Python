termo = int(input('Quantos termos quer mostrar: '))
n1 = 0
n2 = 1
n3 = 0
cont = 0
while cont < termo:
    print(f'{n3} -> ', end=' ')
    n1 = n2
    n2 = n3
    n3 = (n1 + n2)
    cont += 1
print('FIM')