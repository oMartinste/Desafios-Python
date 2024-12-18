peso = float(input('Qual o seu peso (KG): '))
altura = float(input('Qual sua altura: '))
imc = peso / (altura * altura)
print('Seu IMC atual é {:.1f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif 25 > imc >= 18.5:
    print('PESO IDEAL!')
elif 30 > imc >= 25:
    print('SOBREPESO')
elif 40 > imc >= 30:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')