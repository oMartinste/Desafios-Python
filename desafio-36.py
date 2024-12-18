casa = float(input('Qual o valor do imóvel: R$'))
sal = float(input('Qual a sua renda mensal: R$'))
ano = int(input('Quantos anos pretende pagar: '))
pres = casa / (ano * 12)
print('Com seu empréstimo de R${}{:.2f}{}, você pagará por mês, R${}{:.2f}{}'.format('\033[32m', casa, '\033[m', '\033[32m', pres, '\033[m '))
if pres > (sal / 100 * 30):
    print('{}EMPRESTIMO NEGADO!{}'.format('\033[31m', '\033[m'))
else:
    print('{}EMPRESTIMO APROVADO{}, VÁ ATE UMA DE NOSSAS AGÊNCIAS'.format('\033[32m', '\033[m'))