print('{}{}ESCOLHA A BASE DE CONVERSÃO{}{}'.format('\033[33m' ,10*'-', 10*'-', '\033[m'))
print('Escreva\n - {}1{} para {}binário{}\n - {}2{} para {}octal{}\n - {}3{} para {}hexadecimal{}'.format('\033[32m', '\033[m', '\033[32m', '\033[m', '\033[32m', '\033[m', '\033[32m', '\033[m', '\033[32m', '\033[m', '\033[32m', '\033[m'))
n1 = int(input('Escreva um numero para converte-lo: '))
base = int(input('Digite o valor da base de conversão de 1 a 3: '))
if base == 1:
    print('O valor {}BINÁRIO{} de {}, é {}{}{}!'.format('\033[32m', '\033[m', n1, '\033[32m', bin(n1)[2:], '\033[m]'))
elif base == 2:
    print('O valor {}OCTAL{} de {}, é {}{}{}!'.format('\033[32m', '\033[m', n1,  '\033[32m', oct(n1)[2:], '\033[m'))
elif base == 3:
    print('O valor {}HEXADECIMAL{} de {}, é {}{}{}!'.format('\033[32m','\033[m',n1 ,  '\033[32m', hex(n1)[2:], '\033[m'))
else:
    print('{}ERRO! DIGITE UMA BASE VÁLIDA!{}'.format('\033[31m', '\033[m'))