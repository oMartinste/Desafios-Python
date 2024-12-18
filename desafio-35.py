print('-=' * 40)
print('Analisador de Triângulos')
print('-=' * 40)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Esses segmentos FORMAM um TRIÂNGULO!')
else:
    print('Esses segmentos NÃO FORMAM um TRIÂNGULO!')
