n1 = input('Digite um valor:')
print(type(n1))

# logo o valor digitado em n1 é uma string não um numero inteiro

n2 = int(input('Digite outro valor:'))
print(type(n2))

n3 = int(input('Digite um terceiro número:'))
s = n2 + n3

 #print('A soma entre' , n2 , '+' , n3 , 'resulta em' ,s)
print('A soma entre {} e {} é igual a {}'.format(n2, n3, s))

# Agora com o método de formatação int() transformamos o valor de str para int
