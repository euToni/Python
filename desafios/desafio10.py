n = int(input('Quanto você tem na sua carteira? '))
dol = n / 5

print('\033[0;36;41mVocê tem {}R$, então você pode comprar {:.2f}US$\033[m'.format(n, dol))