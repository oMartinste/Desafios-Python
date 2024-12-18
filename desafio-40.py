n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é {}{}{}'.format('\033[34m', media, '\033[m'))
if media < 5:
    print('{}REPROVADO{}'.format('\033[31m', '\033[m'))
elif 7 > media >= 5:
    print('{}RECUPERAÇÃO{}'.format('\033[33m', '\033[m'))
else:
    print('{}APROVADO{}'.format('\033[32m', '\033[m'))