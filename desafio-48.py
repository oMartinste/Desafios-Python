s = 0
cont = 0
for c in range(1, 500):
    if c % 3 == 0:
        if c % 2 == 1:
            cont += 1
            s += c

print(f'A soma de todos os {cont} numeros impares multiplos de 3 é {s}')