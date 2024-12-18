from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
idade = (date.today().year - ano)
if idade <= 9:
    print('Você tem {} anos, sua classe é MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, sua classe é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, sua classe é JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos, sua classe é SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos, sua clase é MASTER!'.format(idade))