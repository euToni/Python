nome = input('Qual é o seu nome?')
idade = int(input('Quantos anos você tem?'))
work = input('Where did you work for?')
mora = input('Onde você mora?')
print('É um prazer em te conhecer {:^10}!'.format(nome))
print('Então você tem {:<10} anos'.format(idade))
print('Oh! so you worked at {:>10}! Good job'.format(work))
print('Você mora em {:=^10}! Legal!'.format(mora))