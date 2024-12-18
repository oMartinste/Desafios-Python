n1 = str(input("Qual o nome da cidade: "))
n2 = n1.upper()
cid = n2.split()
print("Ela começa com a palavra SANTO: {}!".format("SANTO" in cid[0]))