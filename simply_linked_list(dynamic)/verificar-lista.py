#Algoritmo

#Declarar variáveis
#Variável lista

#Verificar se a lista está vazia, caso positivo retornar 'true' se não 'false'

#se (lista.proximo igual a nulo) então
#retornar 'true'
#senão
#retortar 'false'
#fim se


#Classe Nodo
class Nodo:
    def __init__(self, codigo=0, proximo_nodo=None):
        self.codigo = codigo
        self.proximo = proximo_nodo

    def repr (self):
        return '% -> %s' % (self.codigo, self.proximo)

#Classe Lista Encadeada
class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
#Função que verifica a lista
def verifica_vazia(lista):
    if Lista.cabeca == None :
        print("true")
    else:
        print("false")

#Codigo principal
Lista = ListaEncadeada()
verifica_vazia(Lista)

#Saída:
# true