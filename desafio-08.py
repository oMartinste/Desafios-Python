me = float(input("Escreva os metros: "))
km = me * 0.001
hm = me * 0.01
dam = me * 0.1
m = me * 1
dm = me * 10
cm = me * 100
mm = me * 1000
print("{} metro(s) é;\n{} centimetro(s)\n{} milímetro(s)".format(me, cm, mm))
print("{} decimetro(s)\n{} metro(s)\n{} decâmetro(s)".format(dm, m, dam))
print("{} Hectômetro(s)\n{} Quilômetro(s)".format(hm, km))


