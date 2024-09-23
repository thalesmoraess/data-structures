class Deque:
    def __init__(self):
        self.items = []

    def estaVazio(self):
        return self.items == []

    def adicionaFrente(self, item):
        self.items.append(item)

    def adicionaAtras(self, item):
        self.items.insert(0, item)

    def removeFrente(self):
        return self.items.pop()

    def removeAtras(self):
        return self.items.pop(0)
    
    def tamanho(self):
        return len(self.items)

# primeiro, criamos uma deque vazia
d = Deque()

# depos, usamos o método para confirmar se a deque está vazia, transformando em valor booleano para que tenhamos uma resposta "True" ou "False"
print(bool(d.estaVazio))

print(d.tamanho())