soma = cont = n1 = 0
while n1 != 999:
    n1 = int(input('Digite um numero [999 para parar]: '))
    soma += n1
    cont += 1
print(f'Você digitou {cont - 1} números e a soma entre eles foi {soma - n1}.')
