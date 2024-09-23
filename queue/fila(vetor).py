# A seguir, temos o código comentado para a implementação de uma fila usando lista(vetor), em Python

class Fila:
    # cria uma fila vazia
    def __init__(self):
        self._items = list()

    # se a fila estiver vazia retorna True, senão retorna False
    def estaVazia(self):
        return len(self) == 0
    
    # retorna quantos elementos tem na fila
    def __len__(self):
        return len(self._items)

    # insere um elemento na fila
    def enfileira(self, item):
        self._items.append(item)

    # remove e retorna o primeiro elemento da fila
    def desenfileira(self):
        assert not self.estaVazia(), "Fila vazia"
        return self._items.pop(0)

f = Fila()
print(list(f._items))
print(f.estaVazia())
f.enfileira(34)
print(list(f._items))
f.enfileira(26)
print(list(f._items))
print(f.estaVazia())
f.enfileira(44)
print(list(f._items))
f.desenfileira()
print(list(f._items))
f.enfileira(55)
print(list(f._items))
print(f.__len__())
f.enfileira(73)
print(list(f._items))