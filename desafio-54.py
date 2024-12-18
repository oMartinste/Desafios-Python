from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input(f'Qual ano a {i}ª pessoa nasceu : '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'Com base nos dados existe {maior} pessoas adultas e {menor} menores de idade ')
