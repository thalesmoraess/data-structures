class Lista:
    class No:
        def __init__(self, valor, proximo=None):
            self.valor = valor
            self.proximo = proximo

    def __init__(self):
        self.cabeca = None
        self.quantidade = 0

    def __len__(self):
        return self.quantidade

    def inserir(self, posicao, valor):
        novo = self.No(valor)
        self.quantidade += 1

        #quando a lista é vazia
        if self.cabeca is None:
            self.cabeca = novo
            return

        #inserir na cabeça (primeira posiçao)
        if posicao <= 0:
            novo.proximo = self.cabeca
            self.cabeca = novo
            return
        
        i = 0 #índice do elemento atual
        atual = self.cabeca
        #buscando o elemento anterior a posição que a gente quer inserir
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1

        novo.proximo = atual.proximo
        atual.proximo = novo

lista = Lista()

print(len(lista))

lista.inserir(posicao=0, valor=5)
lista.inserir(posicao=1, valor=20)
lista.inserir(posicao=2, valor=15)
lista.inserir(posicao=2, valor=7)
print(len(lista))
