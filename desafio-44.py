produto = float(input('Qual o valor do produto: R$'))
print('CONDIÇÕES DE PAGAMENTO:\n{}[1] DINHEIRO ou CHEQUE\n[2] CARTAO A VISTA\n[3] 2X NO CARTAO\n[4] 3X OU MAIS{}'.format('\033[32m', '\033[m'))
condição = int(input('Qual a condição de pagamento: '))
print('{}Abaixo verá os valores a partir das condições{}'.format(5*'-', 5*'-'))
if condição == 1:
    print('Pagando em DINHEIRO/CHEQUE você tem um desconto de 10%\ncom o produto ficando por R${:.2f}'.format(produto - (produto * 10 / 100)))
elif condição == 2:
    print('Pagando a VISTA NO CARTÃO, você tem um desconto de 5%\ncom o produto ficando por R${:.2f}'.format(produto - (produto * 5 / 100)))
elif condição == 3:
    print('Pagando em 2X NO CARTÃO, o preço se mantém o mesmo\nsendo R${:.2f}'.format(produto))
elif condição == 4:
    print('Pagando em 3x OU MAIS parcelas, o produto fica 20% mais caro\nficando por R${:.2f} '.format(produto * 20 / 100 + produto))
else:
    print('ESCREVA UM CONDIÇAÕ VÁLIDA CONFORME A LISTA!')