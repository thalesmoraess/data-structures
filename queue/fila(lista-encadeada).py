# Aqui, vamos mostrar uma possível implementação em Python usando uma lista encadeada

class FilaListaEncadeada:
    # cria uma fila vazia, utilizando a estrutura de uma lista encadeada
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._contador = 0

    # se a fila estiver vazia retorna True, senão retorna False
    def estaVazia(self):
        return self._inicio is None

    # retorna quantos elementos tem na fila
    def __len__(self):
        return self._contador

    # insere um elemento na fila
    def enfileira(self, item):
        elemento = NoFila(item)
        if self.estaVazia():
            self._inicio = elemento
        else:
            self._fim.next = elemento

        self._fim = elemento
        self._contador += 1

    # remove e retorna o primeiro elemento da fila
    def desenfileira(self):
        assert not self.estaVazia(), "Fila vazia"
        elemento = self._inicio
        if self._inicio is self._fim:
            self._fim = None

            self._inicio = self._inicio.next
            self._contador -= 1
            return elemento.item

# classe privada para armazenamento de nós da lista encadeada
class _NoFila(object):
    def __init__(self, item):
        self.item = item
        self.next = None