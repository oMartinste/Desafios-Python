import math
a = float(input("Qual o comprimento em cm do cateto oposto: "))
b = float(input("Qual o comprimento em cm do cateto adjacente: "))
c = math.hypot(a, b)
print("Com essas informações, o comprimento da hipotenusa é {:.2f}cm".format(c))