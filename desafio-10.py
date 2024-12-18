r = float(input("Qual o valor em reais: R$"))
d = r / 3.27
e = r / 4.27
print("Com {:.2f}R$ você pode comprar\n{:.2f}U$\n{:.2f}€".format(r, d, e))