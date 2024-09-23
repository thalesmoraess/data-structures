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
        
d = Deque()

d.adicionaFrente(1)
print(list(d.items))

d.adicionaFrente(7)
print(list(d.items))

d.adicionaAtras(4)
print(list(d.items))

d.adicionaAtras(8)
print(list(d.items))

d.removeFrente()
print(list(d.items))

d.removeAtras()
print(list(d.items))

print(list(d.items))