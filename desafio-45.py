import random
print('{}JOKENPO{}'.format(15 * '-', 15 * '-'))

itens = ('Pedra', 'Papel', 'Tesoura')
lista = [0, 1, 2]
pc = random.randint(0, 2)

p1 = int(input('Escolha entre:\n[0]PEDRA\n[1]PAPEL\n[2]TESOURA\nPARA JOGAR: '))

if pc == 0 and p1 == 2:
    print('A maquina escolheu {} e você {}, portanto a {}MAQUINA{} ganhou!'.format(itens[pc], itens[p1], '\033[31m', '\033[m'))
elif pc == 1 and p1 == 0:
    print('A maquina escolheu {} e você {}, portanto a {}MAQUINA{} ganhou!'.format(itens[pc], itens[p1], '\033[31m', '\033[m'))
elif pc == 2 and p1 == 1:
    print('A maquina escolheu {} e você {}, portanto a {}MAQUINA{} ganhou!'.format(itens[pc], itens[p1], '\033[31m', '\033[m'))
elif pc == p1:
    print('A maquina escolheu {} e você {}, portanto, {}DEU EMPATE{}!'.format(itens[pc], itens[p1], '\033[33m', '\033[m'))
elif p1 != lista :
    print('{}ESCREVA CORRETAMENTE!{}'.format('\033[33m', '\033[m'))
else:
    print('A maquina escolheu {} e você {}, portanto {}VOCÊ{} ganhou {}PARABÉNS{}!'.format(pc, p1, '\033[32m', '\033[m', '\033[32m', '\033[m'))
print('{}JOGUE DE NOVO!{}'.format('\033[32m', '\033[m'))