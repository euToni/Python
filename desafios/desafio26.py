frase = str(input('Digite uma frase: ')).upper().strip() #strip retira os espaços, e upper joga tudo para maiusc
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
