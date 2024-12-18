s = 0
for i in range(0,6):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        s += n1
print(f'A soma dos numeros pares que você indicou é {s}')