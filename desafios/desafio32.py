ano = int(input('Digite um ano qualquer: '))
if ano % 4 == 0:
    print('O ano {} é um ano BISSEXTO!'.format(ano))
else:
    print('Apenas mais um ano comúm de 365 dias')