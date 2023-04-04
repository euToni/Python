import random
numero = int(input('Chute um número inteiro entre 1 e 10: '))
n = random.randrange(1, 10)
if numero == n:
    print('Parabéns você acertou!')
else:
    print('Game over')
print('O número correto é {}'.format(n))
