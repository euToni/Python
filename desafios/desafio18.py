#SENO COSSENO E TANGENTE DE UM ANGULO

import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
print('O angulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = math.cos(math.radians(an))
print('O cosseno é {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(an))
print('A tangente é {:.2f}'.format(tangente))