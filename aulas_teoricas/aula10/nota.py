n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('Sua média anual é de {:.1f}'.format(media))
if media < 5:
    print('Está de recuperação')
else:
    print('Boa, passou de ano!')