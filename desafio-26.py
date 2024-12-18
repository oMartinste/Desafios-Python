nome = str(input("Digite seu nome: ")).strip().lower()
print("A letra A, aparece {}x no seu nome!".format(nome.count("a")))
print("Ela aparece na posição {} pela primeira vez!".format(nome.find("a")+1))
print("Ela aparece na posição {} pela última vez!".format(nome.rfind("a")+1))