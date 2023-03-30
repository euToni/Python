dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))
valord = dias * 60
valorkm = km * 0.15
valorf = valord + valorkm

print('O total a pagar é de {:.2f}R$'.format(valorf))
