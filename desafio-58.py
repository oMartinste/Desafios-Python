import random
pc = random.randint(0, 10)
user = 0
tot = 0
print('Eu sou seu computador, acabei de pensar em um numero entre 0 e 10')
print('Vamos adivinhar o numero que estou pensando!')
while user != pc:
    user = int(input('Qual o seu palpite: '))
    tot += 1
    if user == pc:
        print(f'PARABÉNS, você acertou o numero que a maquina escolheu, com um total de {tot} tentativas!')
    else:
        if user < pc:
            print('Mais... Você errou, tente novamente!')
        elif user > pc:
            print('Menos... Você errou, tente novamente!')


