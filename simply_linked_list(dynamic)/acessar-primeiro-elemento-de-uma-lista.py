#Algoritmo
#Declarar uma variável do tipo Nodo
#Variavel None Nd

#Atribuir um elemento na lista
#Nd = lista.proximo

#Realizar a impressão do Nodo
#imprime Nd

#Classe Nodo
class Nodo:
    def __init__(self, codigo=0, proximo_nodo=None):
        self.codigo = codigo
        self.proximo = proximo_nodo

    def __repr__(self):
        return '% -> %s' % (self.codigo, self.proximo)

#Classe Lista Encadeada
class ListaEncadeada:

    def __init__(self):
        self.cabeca = None
        
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

#Código principal
lista = ListaEncadeada()
Primeiro = lista.cabeca
print(Primeiro)

#Saída:
# None
# Como a lista está vazia retorna Vazio - None