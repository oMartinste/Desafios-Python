media = 0
maioridade = 0
nomevelho = 0
totm = 0
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media += idade
    if p == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totm += 1

print(f'A media de idade do grupo é de {media / 4} anos.')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}.')
print(f'Ao todo são {totm} mulheres com menos de 20 anos.')

