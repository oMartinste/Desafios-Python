import math
ang = int(input("Qual o angulo: "))
rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print("O angulo {} Graus tem como;\n seno: {},\ncosseno: {}\ntangente: {}".format(ang, seno, cosseno, tangente))