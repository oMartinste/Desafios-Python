n = input("Escreva algo: ")
print("O tipo primitivo desse valor é: {}!".format(type(n)))
print("É numérico: {}!",n.isnumeric())
print("É numérico ou alfabético: {}!",n.isalnum())
print("É alfabético: {}!",n.isalpha())
print("É maiúsculo: {}!".format(n.isupper()))
print("Pode ser impresso: {}!".format(n.isprintable()))
print("É minúsculo: {}!".format(n.islower()))