sal = int(input('Qual é o seu atual salário atual? '))
aumento = sal / 10 
vfinal = aumento + aumento / 2 + sal

print('Você estava merecendo um aumento, então receba 15% \n Seu salário atual agora é {}R$'.format(vfinal))