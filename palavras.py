import random

class Palavras:
    def lista_palavras(self):
        palavras = ['ABACATE','BANANA', 'LARANJA', 'MELANCIA', 'UVA', 'GOIABA']
        tamanho = len(palavras)
        indice = random.randint(0, tamanho-1)
        return palavras[indice]
        
        
