import palavras
# 0
#/|\
#/-\
def desenho_forca():
    print('-----')
    i =1
    print('|    |')
    for i in range(4):
        print('|')
        
def imprime_espaco(palavra_digitada):
     for i in range(len(palavra_digitada)):
        print(palavra_digitada[i],end=" ")
     print()
    
def jogo():
    p = palavras.Palavras()
    palavra_secreta = p.lista_palavras()
    tamanho_palavra = len(palavra_secreta)
    palavra_digitada = []
    acertou = errou = False
    corpo = 0

    for i in range(tamanho_palavra):
        palavra_digitada.append("_")
    print('A palavra tem ', tamanho_palavra, 'letras')
    imprime_espaco(palavra_digitada)


    while not acertou and not errou:
        chute = input('Digite uma letra: ')
        if chute.upper() in palavra_secreta:
            print('acertou')
            posicao = 0
            for letra in palavra_secreta:
                if chute.upper() == letra:
                    palavra_digitada[posicao] = letra
                posicao += 1
            
        else:
            print('Essa letra não está na palavra')
            corpo+= 1
        imprime_espaco(palavra_digitada)

        errou = corpo == 7
        acertou = '_' not in palavra_digitada

    if acertou:
        print('Parabéns, você descobriu a palvra!')
    else:
        print('Você não descobriu a palavra, mais sorte na próxima!')
        
    


if __name__ == '__main__':
    print('Vamos jogar')
    desenho_forca()
    jogo()
