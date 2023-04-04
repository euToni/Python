sal = float(input('Qual é o seu salário atual? '))
extra = sal + (sal * 10/100)
plus = sal + (sal * 15/100)

if sal <= 1250:
    print('Seu salário atual é de R${:.0f}, com o aumento, passa a ser R${:.2f}'.format(sal, plus))
else:
    print('Seu salário atual é de R${:.0f}, com o aumento, passa a ser R${:.2f}'.format(sal, extra))
print('Parabéns pelo Aumento 😉')