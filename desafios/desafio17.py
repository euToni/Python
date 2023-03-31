import math
cate = float(input('Qual o valor do cateto?: '))
adja = float(input('E do cateto adjacente?: '))
hipo = cate **2 + adja ** 2
vhipo = math.sqrt(hipo) 
print('O valor da hipotenusa é {:.0f}'.format(vhipo))