'''
a1 = input('Digite uma frase: ').strip().lower()
list = a1.split()
separacao = ''.join(list)
inverso = separacao[::-1]
print(f'O inverso de {a1.upper()} é {inverso.upper()} ')
if inverso == separacao:
    print(f'A frase {a1.title()} é um palindromo!')
else:
    print(f'A frase {a1.title()} não é um palindromo!')
'''
a1 = input('Digite uma frase: ').strip().lower()
list = a1.split()
junto = ''.join(list)
inverso = ''
print(f'O inverso de {a1.upper()} é {inverso.upper()} ')
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada NÃO é um PALÍNDROMO')

