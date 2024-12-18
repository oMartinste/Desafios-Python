
p1 = int(input('Digite o PRIMEIRO TERMO dessa PA: '))
raz = int(input('Digite a RAZÃO dessa PA: '))
dec = p1 + (10-1) * raz
for p in range(p1, dec, raz):
   print(p)
