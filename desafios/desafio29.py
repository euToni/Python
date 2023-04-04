vel = int(input('Qual era a velocidade do veículo? '))
n1 = vel - 80
n2 = n1 * 7
if vel > 80:
    print('Infelizmente, o senhor(a), foi MULTADO!')
    print('Sua multa foi de {}R$'.format(n2))
else:
    print('Dirija sempre com cuidado!')
