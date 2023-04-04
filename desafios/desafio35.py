a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Só mais um: '))
if a + b > 3 and b + c > a and c + a > b:
    print('É possível formar um tríangulo com esses valores...')
else:
    print('Não é possível formar um tríangulo..')