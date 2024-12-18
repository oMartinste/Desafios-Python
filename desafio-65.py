soma = cont = media = menor = maior = 0
continuar = 'S'
while continuar == 'S':
    n1 = int(input('Digite um numero: '))
    soma += n1
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'Você digitou {cont} numeros e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')