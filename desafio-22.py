n1 = str(input("Escreva seu nome completo: "))
print("Somente maiúsculas: {}!".format(n1.upper()))
print("Somente minúsculas: {}!".format(n1.lower()))
n2 = n1.split()
nome = "".join(n2)
print("O nome tem {} letras.".format(len(nome)))
print("O Primeiro nome tem {} letras!".format(len(n2[0])))