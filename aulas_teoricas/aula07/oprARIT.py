n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
r = n1 % n2
de = n1 // n2
p = n1 ** n2
raiz = n1 **(1/2) 

print('A soma é {}, \n o produto é {}, \n a divisão é {:.2f}'.format(s, m, d), end=' ') 
print('Divisão inteira é {} potência é {} a subtração fica {}'.format(de, p, sub), end=' ')
print('O resto da divisão fica {} e a raiz do primeiro número é {}'.format(r, raiz), end=' ')