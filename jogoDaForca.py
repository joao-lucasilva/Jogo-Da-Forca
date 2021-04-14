def jogo():
    palavras = ['Banana', 'Abacate']
    palavra_digitada = ""
    espaco = []
    corpo = 0
# 0
#/|\
# |
#/-\
    print('A palavra tem ', len(palavras[0]), 'letras')
    for i in range(len(palavras[0])):
        espaco.append("_")
        print(espaco[i],end=" ")
    print()


    while palavra_digitada != palavras[0] or corpo < 8:
        letra = input('Digite uma letra: ')
        if letra in palavras[0]:
            print('acertou')
            palavra_digitada = letra
        else:
            print('Essa letra não está na palavra')
            corpo += 1
    
def desenho_forca():
    print('-----')
    for i in range(4):
        if i == 0:
            print('|    |')
        else:
            print('|')

if __name__ == '__main__':
    print('Vamos jogar')
    desenho_forca()
    jogo()