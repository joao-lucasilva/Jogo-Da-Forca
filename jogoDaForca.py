palavras = ['Banana', 'Abacate']
espaco = []
print('Vamos jogar')

print('A palavra tem ',len(palavras[0]), 'letras')
for i in range(len(palavras[0])):
    espaco.append("_")
    print(espaco[i],end=" ")
print()
letra = input('Digite uma letra: ')

if letra in palavras[0]:
    print('acertou')
    
