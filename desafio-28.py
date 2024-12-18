import random
n1 = random.randint(0, 5)

user = int(input('Qual o numero sorteado: '))
if user == n1:
    print('Você acertou!!!')
else:
    print('Você errou!!! Tente novamente.')
print('O numero sorteado foi {}!'.format(n1))