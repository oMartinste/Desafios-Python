vel = float(input('Qual a velocidade do veiculo: '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você foi multado em R${}'.format(multa))
else:
    print('Continue dirigindo com prudência!')
