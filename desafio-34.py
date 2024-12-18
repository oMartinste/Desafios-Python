sal = float(input('Qual o seu salário R$'))
a1 = (sal / 100 * 10) + sal
a2 = (sal / 100 * 15) + sal

if sal <= 1250:
    print('O seu salário de {:.2f}, aumentou 15%, totalizando R${:.2f}!'.format(sal ,a2))
else:
    print('O seu salário de {:.2f}, aumentou 10%, totalizando R${:.2f}!'.format(sal, a1))