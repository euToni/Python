frase = 'Curso em Vídeo Python'
print(frase[14:]) #Mostrando a frase a partir do caracter 14 até o fim (python)

print(frase.upper().count('O')) #jogando a string para maiuscula e contando os 'O' q tem

print(len(frase.strip())) #verificando o comprimento da string e removendo os espaços inuteis com o strip()

print(frase.replace('Python', 'Brimstonne')) #trocando a plavra python por brims...

print('Curso' in frase) #verificando se há a palavra curso na var

print(frase.find('Vídeo')) #verificando o indice da palavra video na var

print(frase.split()) #mostrando a frase dividida em lista

div = frase.split() #guardando o valor da divisão da frase em uma var

print(div[0] [3]) #mostrando apenas a 3 letra da palavra de indice 0 da var frase