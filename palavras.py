import random

class Palavras:
    def lista_palavras():
        palavras = ['ABACATE','BANANA', 'LARANJA', 'MELANCIA', 'UVA', 'GOIABA']
        tamanho = len(palavras)
        indice = random.randeint(0, tamanho)
        return palavras[indice]
        
        
