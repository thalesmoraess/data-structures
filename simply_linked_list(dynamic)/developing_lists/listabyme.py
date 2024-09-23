# CRIAÇÃO DE UM NOVO
# classe Nodo
class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.conteudo, self.proximo)

# programa principal de teste
Nd = Nodo()
print(Nd)

Nd2 = Nodo("casa")
print(Nd2)


# CRIAÇÃO DA CLASSE ListaEncadeada
# classe lista encadeada
class ListaEncadeada:

    def __init__(self):
        self.inicio = None

    def __repr__(self):
        return "[" + str(self.inicio) + "]"

# programa principal de teste
lista = ListaEncadeada()
Nd = Nodo("Primeiro")
lista.inicio = Nd
print(lista)


#CRIAÇÃO DA FUNÇÃO ListaVazia
# método que verifica se a lista está vazia, caso positivo retorna True caso contrário False
def ListaVazia(Lista):
    if Lista.inicio == None :
        return True
    else:
        return False

# programa principal de teste
lista = ListaEncadeada()
print("A lista está vazia: ", ListaVazia(lista))

Nd = Nodo("Primeiro")
lista.inicio = Nd

print("A lista está vazia: ", ListaVazia(lista))


# CRIAÇÃO DO MÉTODO TamanhoLista
# método que informa o tamanho da lista
def TamanhoLista(self):
    atual = self.inicio
    tamanho = 0

    # verifica se a lista está vazia e já retorna com Zero
    if self.inicio == None:
        return 0

        # verifica se a lista possui somente um elemento    
        if atual.conteudo != None and atual.proximo == None:
            tamanho = 1

        # percorre toda a lista até o último nodo ser vazio, incrementando +1 em casa Loop e passando para a posição do próximo nodo
        while atual.proximo != None:
            tamanho = tamanho+1
            atual = atual.proximo
        
        return tamanho

# programa principal de teste
lista = ListaEncadeada()
Nd = Nodo("Primeiro")

# adiciona 1 elemento na lista
lista.inicio = Nd

print("O tamanho da lista: ", TamanhoLista(lista))

# CRIAÇÃO DA FUNÇÃO Adiciona_Inicio
# método que adiciona um elemento no início da lista
def Adiciona_Inicio(self, Nd):

    # cria o nodo com o 1 elemento da lista
    atual = self.inicio
    # atribui ao novo nodo o primeiro elemento da lista
    Nd.proximo = atual
    #atualiza o primeiro elemento da lista como sendo o novo elemento
    self.inicio = Nd

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Inicio(lista, Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Inicio(lista,Nd2)
print("lista: ", lista)

# CRIAÇÃO DA FUNÇÃO Adiciona_Fim
def Adiciona_Fim(self, item):

    # verifica se a lista não está vazia para percorrer, pois, se estiver, irá adicionar no início
    if self.inicio:
        aux = self.inicio
        # percorre a lista até o último elemento
        while (aux.proximo):
            aux = aux.proximo
        # quando sair do laço é porque chegou no último elemento; Logo, atualiza o último elemento a receber como proximo o novo elemento
        aux.proximo = item
    # como a lista está vazia, adiciona no início da lista
    else:
        self.inicio = item

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Fim(lista,Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Fim(lista,Nd2)
print("lista: ", lista)

Nd3 = Nodo("C")
Adiciona_Fim(lista,Nd3)
print("lista: ", lista)

# CRIAÇÃO DA FUNÇÃO Adiciona_Pos
def Adiciona_Posicao(self,item,pos):
    atual = self.inicio
    pos_atual = 0

    # percorre até o final da lista
    while atual.proximo != None:

        # verifica se a posição atual é anterior à posição desejada
        if pos_atual == (pos-1):
            # realiza a troca dos ponteiros e insere o novo elemento
            pointer = atual
            item.proximo = pointer.proximo
            pointer.proximo = item
        else:
            atual = atual.proximo

        pos_atual = pos_atual + 1

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Inicio(lista,Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Inicio(lista,Nd2)
print("lista: ", lista)

Nd3 = Nodo("C")
Adiciona_Posicao(lista,Nd3,1)
print("lista: ", lista)


# CRIAÇÃO DA FUNÇÃO Remove_Pos
def Remove_Pos(self,pos):
    atual = self.inicio
    pos_atual = 0

    # verifica se a posição a ser removida é a primeira; se positivo, atualiza o elemento de início da lista
    if pos_atual == pos:
        self.inicio = atual.proximo
    # se a posição a ser removida não é a primeira, percorre a lista até achar a posição anterior à desejada para a troca dos ponteiros
    else:
        while atual.proximo != None:

            if pos_atual == (pos-1):
                next = atual.proximo
                atual.proximo = next.proximo
            else:
                atual = atual.proximo

            pos_atual = pos_atual + 1

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Fim(lista,Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Fim(lista,Nd2)
print("lista: ", lista)

Nd3 = Nodo("C")
Adiciona_Fim(lista,Nd3)
print("lista: ", lista)

Remove_Pos(lista,2)
print("lista: ", lista)

Remove_Pos(lista,0)
print("lista: ", lista)

# CRIAÇÃO DA FUNÇÃO Remove_Inicio
def Remove_Inicio(self):

    # realiza a atribuição
    atual = self.inicio
    # informa para a lista que o seu primeiro elemento é o elemento posterior ao elemento atribuído anteriormente
    self.inicio = atual.proximo

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Fim(lista,Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Fim(lista,Nd2)
print("lista: ", lista)

Nd3 = Nodo("C")
Adiciona_Fim(lista,Nd3)
print("lista: ", lista)

Remove_Inicio(lista)
print("lista: ", lista)

Remove_Inicio(lista)
print("lista: ", lista)

Remove_Inicio(lista)
print("lista: ", lista)

# CRIAÇÃO DA FUNÇÃO Remove_Fim
def Remove_Ultimo(self):
    atual = self.inicio

    # percorre toda a lista de elementos
    while atual.proximo != None:
        # atribui o proximo elemento a uma variável temporária
        proximo = atual.proximo
        # verifica se a variável temporária não possui nodo posterior; se positivo, ele é o último elemento
        if proximo.proximo == None:
            # atualiza o elemento anterior ao temporário com o seu próximo Nulo
            atual.proximo = None
        else:
            atual = atual.proximo

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Fim(lista, Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Fim(lista, Nd2)
print("lista: ", lista)

Nd3 = Nodo("C")
Adiciona_Fim(lista, Nd3)
print("lista: ", lista)

Remove_Ultimo(lista)
print("lista: ", lista)

# CRIAÇÃO DA FUNÇÃO Ocorrência
def Ocorrencia(self,dado):
    atual = self.inicio
    total_ocorrencia = 0

    # percorre toda a lista em busca do elemento
    while atual != None:
    # caso o elemento seja encontrado, deverá adicionar +1 no contador
        if atual.conteudo == dado:
            total_ocorrencia = total_ocorrencia +1
            atual = atual.proximo
        else:
            atual = atual.proximo
    # após percorrer toda a lista, retornar o total de elementos encontrados
    return total_ocorrencia

# programa principal de teste
lista = ListaEncadeada()

Nd = Nodo("A")
Adiciona_Fim(lista, Nd)
print("lista: ", lista)

Nd2 = Nodo("B")
Adiciona_Fim(lista, Nd2)
print("lista: ", lista)

Nd3 = Nodo("A")
Adiciona_Fim(lista, Nd3)
print("lista: ", lista)

print("Ocorrencias da letra A: ", Ocorrencia(lista, "A"))