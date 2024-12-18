primo = int(input('Digite um numero: '))
tot = 0
for p in range(1, primo + 1):
    if primo % p == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{p}', end=' ')
print(f'\nO numero {primo} foi dividido {tot} vezes')
if tot == 2:
    print(f'Sendo assim o numero {primo} é PRIMO')
else:
    print(f'Sendo assim o numero {primo} NÃO é PRIMO')