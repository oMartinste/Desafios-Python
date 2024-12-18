l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Com essas medidas, {}PODEMOS{} formar um {}TRIANGULO{}'.format('\033[32m', '\033[m', '\033[32m', '\033[m'))
    if l1 == l2 == l3:
        print('Essas medidas formam um triangulo {}EQUILÁTERO{}'.format('\033[32m', '\033[m'))
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Essas medidas formam um triangulo {}ISÓSCELES{}'.format('\033[32m', '\033[m'))
    elif l1 != l2 != l3 != l1:
        print('Essas medidas formam um triangulo {}ESCALENO{}'.format('\033[32m', '\033[m'))
else:
    print('Com essas medidas {}NÃO PODEMOS{} formar um {}TRIANGULO{}'.format('\033[31m', '\033[m', '\033[31m', '\033[m'))

