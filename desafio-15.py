alug = int(input("Quantos dias alugados: "))
km = int(input("Quantos Km rodados: "))
dia = alug * 60
rod = km * 0.15
soma = dia + rod
print("O total a pagar é de R${:.2f}".format(soma))