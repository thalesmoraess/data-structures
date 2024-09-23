#Algoritmo

#Declarar variáveis
#Variavel Node NdAnterior
#Variavel Node NdAtual
#Variavel Node NdExcluir
#Variavel inteiro posicao

#Atribuir valores iniciais
#posicao = 10
#NdAnterior = lista
#NdAtual = lista.proximo

#Percorrer lista até encontrar o elemento nulo, logo final da lista enquanto Nd diferente nulo

#enquanto NdAtual.proximo diferente nulo

#Achou o elemento para excluir
#se NdAtual.proximo igual a NdExcluir
#NdAnterior.proximo = NdAtual.proximo

#Libera a memoria
#liberaMemoria(NdAtual)
#sair
#fim se

#Atualiza as variáveis atual e anterior para a próxima interação do laço
#NdAnterior = NdAtual
#NdAtual = NdAtual.proximo

#fimenquanto


#Método 1

def remover(self,pos):
    atual = self.inicio
    post_atual = 0

    while atual.proximo != None:

        if post_atual == (pos-1):
            next = atual.proximo
            atual.proximo = next.proximo
        else:
            atual = atual.proximo

    post_atual = post_atual + 1

#Método 2

lista = [1, 2, 3, 4]
lista.pop(2)
print(lista)

#Saída:
#[1, 2, 4]