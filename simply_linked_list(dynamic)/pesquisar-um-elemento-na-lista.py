#Algoritmo

#Declarar variáveis
#Variável Node Nd
#Variável inteiro cont
#Variável Node NdReferencia

#Atribuir valores iniciais
#Cont = 0
#Nd = lista.proximo
#NdReferencia.dado = 5

#Percorrer lista até encontrar o elemento nulo, logo no final da lista

#Enquanto Nd diferente nulo

#Quando achar um nodo com o conteúdo igual ao nodo de referência, é um nodo que estamos procurando e informamos a sua posição

#se Nd.dado igual a NdReferencia.dado
    #imprime Cont
#fimse

#Cont = cont +1
#Nd = lista.proximo
#fim enquanto

#Método 1 - função que retorna se achou um elemento em uma lista

def ExisteNodo(self,item):
    atual = self.inicio
    status = False
    while atual != None and not status:
        if atual.inf()==item:
            status = True
        else:
            atual + atual.proxNodo()
        return status