from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
anoatual = date.today().year
idade = (anoatual - ano)
if idade < 18:
    print('Ainda falta {} anos para você se alistar!'.format(18 - idade))
elif idade == 18:
    print('Vá a uma junta militar para se alistar!')
elif idade > 18:
    print('Você passou {} anos do seu periodo de alistamento! VÁ ATÉ UMA JUNTA MILITAR E REGULARIZE'.format(idade - 18))
