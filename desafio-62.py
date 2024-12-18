print('GERADOR DE PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
termo2 = 10
while termo2 != 0:
    total += termo2
    while cont <= total:
        print(f'{termo} -> ', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    termo2 = int(input('\nQuantos termos você quer mostrar mais: '))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados.')
