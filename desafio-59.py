menu = 0
p1 = int(input('Primeiro valor: '))
p2 = int(input('Segundo valor: '))
sum = p1 + p2
mult = p1 * p2

while menu != 5:
    print('=-=' * 10)
    print('Você quer fazer oque com esses valores;')
    print('''   [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    menu = int(input('Digite sua escolha: '))
    if menu == 1:
        print(f'A soma dos valores {p1} + {p2} é {sum}')
    elif menu == 2:
        print(f'A multiplicação dos valores {p1} x {p2} é {mult}')
    elif menu == 3:
        if p1 > p2:
            print(f'O maior entre {p1} e {p2} é {p1}')
        else:
            print(f'O maior entre {p1} e {p2} é {p2}')
    elif menu == 4:
        print('=-=' * 10)
        print('Informe os numeros novamente')
        p1 = int(input('Primeiro valor: '))
        p2 = int(input('Segundo valor: '))
    else:
        print('Opção invalida - Tente novamente!')
    print('=-=' * 10)
print('Fim do programa!')







