sal = float(input("Qual o salário atual: "))
aum = sal + (sal / 100 * 15)
print("Salário de {:.2f}R$ passará para {:.2f}R$ com o aumento de 15%".format(sal, aum))
