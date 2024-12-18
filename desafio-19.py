import random
a = str(input("Qual o primeiro aluno: "))
b = str(input("Qual o segundo aluno: "))
c = str(input("Qual o terceiro aluno: "))
d = str(input("Qual o quarto aluno: "))
alunos = [a, b, c, d]
sort = random.choice(alunos)
print("O aluno sorteado é {}!".format(sort))
