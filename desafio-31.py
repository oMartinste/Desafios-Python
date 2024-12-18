dist = float(input('Qual a distância da viagem em Km: '))
d1 = (dist * 0.50)
d2 = (dist * 0.45)
if dist > 200:
    print('O valor da sua viagem vai ficar R${:.2f}!'.format(d2))
else:
    print('O valor da sua viagem vai ficar R${:.2f}!'.format(d1))
print('BOA VIAGEM!')


