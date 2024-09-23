#Algoritmo

#Declarar variáveis
#Variável Node Nd
#Variável inteiro posição
#Variável inteiro cont
#Variável Node Ndnovo
#Variável Node temp

#Atribuir valores iniciais
#cont = 0
#Nd = lista.proximo
#NdNovo.dado = 5
#posição = 10

#Percorrer lista até encontrar o elemento nulo, logo final da lista enquanto Nd diferente nulo

#enquanto lista.proximo diferente nulo

#Se o contador encontra-se na posição desejada realizar a inserção do nodo

#se cont igual a posição
#temp= lista.proximo
#lista.proximo= Ndnovo
#Ndnovo.proximo= temp
#fimse

#fimenquanto


#Método 1

def inserir(self,item,pos):
    atual = self.inicio
    pos_atual = 0

    while atual.proximo != None:

        if pos_atual == (pos-1):
            pointer = atual
            node = node(item)
            node.proximo = pointer.proximo
            pointer.proximo = node
        
        else:
            atual = atual.proximo
    
    pos_atual = pos_atual + 1

#Método 2

lista = [1, 2, 3, 4]
lista.insert(2, 10)
lista.insert(5, 7)
print(lista)

#Saída:
# [1, 2, 10, 3, 4]