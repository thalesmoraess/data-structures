# ALGORITMO
# criar as classes
# criar os métodos de impressão e Nova Bagagem
# criar o método de Peso Total
# realizar os testes dos métodos anteriores

class Bagagem:
    def __init__(self, Codigo = "indefinido", Peso = 0):
        self.Codigo = Codigo
        self.Peso = Peso

    def __repr__(self):
        return '%s -> %d' % (self.Codigo, self.Peso)

class Nodo:
    class Nodo:
        def __init__(self, dado = 0, proximo_nodo = None):
            self.conteudo = dado
            self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.conteudo, self.proximo)

class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    def __repr__(self):
        return "[" + str(self.inicio) + "]"

    def ListaVazia(self):
        if self.inicio == None:
            return True
        else:
            return False
        
    # método de impressão percorre toda a lista realizando a impressão de cada Nodo do tipo Bagagem
    # para facilitar a compreensão foi utilizado uma variável cont para informar a posição da Bagagem na Lista
    def ImprimeLista(self):
        atual = self.inicio

        cont = 0
        print("Inicio da lista")
        if self.inicio == None:
            print("Lista vazia")
        else:
            while atual != None:
                print("Posição: ",cont, atual)
                cont = cont + 1
                atual = atual.proximo
        print("Final da lista")

    # método que adiciona no inicio de cada nova bagagem. este método foi escolhido por possuir o menor número de comparações, logo menor consumo de processamento
    def NovaBagagem(self, Nd):

        # cria o nodo com o 1 elemento da lista
        atual = self.inicio
        # atribui ao novo nodo o primeiro elemento da lista
        Nd.proximo = atual
        # atualiza o primeiro elemento da lista como sendo o novo elemento
        self.inicio = Nd
    
    # método que percorre toda a lista realizando a soma da variável Peso em cada nodo, caso a lista esteja vazia retorna 0
    def PesoTotal(self):
        atual = self.inicio
        peso = 0

        if self.inicio == None:
            return 0
        
        while atual != None:
            peso = peso + atual.Peso

            atual = atual.proximo
        
        return peso
    
# programa principal de teste

# declaração da lista vazia
lista = ListaEncadeada()

# criação dos Nodos do tipo Bagagem e adicionados na lista
lista.NovaBagagem(Bagagem("001",10))
lista.NovaBagagem(Bagagem("002",15))
lista.NovaBagagem(Bagagem("003",25))
lista.NovaBagagem(Bagagem("004",20))
lista.NovaBagagem(Bagagem("005",30))

# chamada de método de impressão da lista desenvolvido para verificação se for realizado como provisto
lista.ImprimeLista()

# impressão do total de bagagens da lista com o objetivo de verificar se realizou o cálculo corretamente
print("Peso total: ", lista.PesoTotal())