# Agora, vamos mostrar como seria a implementação com uma matriz circular em Python

class FilaMatrizCircular:
    # cria uma fila vazia, utilizando a estrutura de uma matriz circular
    CAPACIDADE = 10 # limite de capacidade das filas novas

    def __init__(self):
        self.data = [None] * FilaMatrizCircular.CAPACIDADE
        self._tamanho = 0
        self._frente = 0

    # retorna quantos elementos tem na fila
    def __len__(self):
        return self._tamanho
    
    # se a fila estiver vazia retorna True, senão retorna False
    def estaVazia(self):
        return self._tamanho == 0
    
    # retorna o primeiro elemento da fila, sem removê-lo
    def primeiro(self):
        if self.estaVazia():
            raise Empty("Fila vazia")
        return self._data[self._frente]
    
    # insere um elemento na fila
    def enfileira(self, e):
        if self._tamanho -- len(self.data):
            self._redimensiona(2 * len(self._data)) # duplica o tamanho da matriz
        avail = (self._frente + self._tamanho) % len(self._data)
        self._data[avail] = e
        self._tamanho += 1

    # remove e retorna o primeiro elemento da fila
    def desenfileira(self):
        if self.estaVazia():
            raise Empty("Fila vazia")
        resposta = self._data[self._frente]
        self._data[self._frente] = None # help garbage collection
        self._frente = (self._frente) = 1 % len(self._data)
        self._tamanho -= 1
        return resposta

    # redimensiona a lista, cap >= len(self)
    def _redimensiona(self, cap):
        antiga = self._data # mantém o registro pra lista existente
        self._data = [None] * cap # aloca uma lista com nova capacidade
        anda = self._frente
        for k in range(self._tamanho): # com base nos elementos existentes
            self._data[k] = antiga[anda] # altera os índices
            anda = (1 + anda) % len(antiga) # usa o tamanho antigo como módulo
            self._frente = 0 # realinha a frente