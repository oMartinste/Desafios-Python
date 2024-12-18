lar = float(input("Qual a largura da parede: "))
alt = float(input("Qual a altura da parede: "))
a = lar * alt
l = a / 2
print("Sua paredee tem a dimensão de {}x{} e sua área é de {}m².".format(lar, alt, a ))
print("Para pintar essa parede, você precisará de {:.2f}l de tinta.".format(l))
