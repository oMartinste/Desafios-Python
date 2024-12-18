pre = float(input("Qual o valor do produto: "))
desc = pre - (pre / 100 * 5)
print("O produto de {}R$ ficou {}R$ com 5% de desconto!".format(pre, desc))
