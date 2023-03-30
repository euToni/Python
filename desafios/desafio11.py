altura = float(input('Quanto de altura tem sua parede? '))
largura = float(input('Quanto de largura tem sua parede? '))
area = altura * largura
tinta = area / 2

print('Sua parede tem {}x{} e sua área é de {}m²'.format(altura, largura, area))
print('Para pintar sua parede você vai precisar de {}L de tinta'.format(tinta))