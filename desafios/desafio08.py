metro = int(input('Valor em metros do produto: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm =  metro* 10
cem = metro * 100
mil = metro * 1000

print('\033[1;33;47mA medida de {}m corresponde a: \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(metro, km, hm, dam, dm, cem, mil))