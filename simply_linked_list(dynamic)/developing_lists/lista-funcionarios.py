class Funcionario:
    def __init__(self, Nome = "indefinido", Codigo = "indefinido", Departamento = "indefinido"):
        self.Nome = Nome
        self.Codigo = Codigo
        self.Departamento = Departamento

    def __repr__(self):
        return '%s -> %s -> %s' % (self.Codigo, self.Departamento, self.Nome)

class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
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

    # método de impressão percorre toda a lista até o final, realizando a impressão de casa Nodo do tipo funcionário
    # para facilitar a compreensão, foi utilizado uma variável cont para informar a posição do usuário na lista
    def ImprimeLista(self):
            atual = self.inicio

            cont = 0
            print("Inicio da lista")
            if self.inicio == None:
                print ("Lista vazia")
            else:
                while atual != None:
                    print("Posição: ", cont, atual)
                    cont = cont + 1
                    atual = atual.proximo
            print("Final da lista")

    # métodos reutilizados a partir da função anterior que conta o número de elementos de uma Lista, no qual somente foi renomeada de TamanhoLista para Numero_Funcionarios
    def Numero_Funcionarios(self):
        atual = self.inicio
        tamanho = 0

        if self.inicio ==  None:
            return 0
        
        while atual != None:
            tamanho = tamanho + 1
            atual = atual.proximo

        return tamanho

    # métodos reutilizadosa partir da função Adiciona_Fim sem modificações, o nome foi atualizado de Adiciona_Fim para Novo_Funcionario
    def NovoFuncionario(self, Nd):

        # cria o nodo com o 1 elemento da lista
        atual = self.inicio
        # atribui ao novo nodo o primeiro elemento da lista
        Nd.proximo = atual
        # atualiza o primeiro elemento da lista como sendo o novo elemento
        self.inicio = Nd

    # método adaptado a partir da função Remove_Pos, substituindo a posição a ser removida pelo conteúdo do objeto
    def Remove_Funcionario(self, Func):
        atual = self.inicio
        pos_atual = 0

        # verifica se a posição a ser removida é a primeira; se positivo, atualiza o elemento de início da Lista
        if atual == Func:
            self.inicio = atual.proximo

        # se a posição a ser removida não é a primeira, percorre a Lista até achar a posição anterior à desejada para a troca dos ponteiros
        else:
            while atual.proximo != None:
                next = atual.proximo

                if next == Func :
                    atual.proximo = next.proximo
                else:
                    atual = atual.proximo

# programa principal de teste

# declaração da Lista vazia
lista = ListaEncadeada()

# criação de nodos do tipo funcionario
# estes nodos poderiam ser oriundos de uma busca do banco ou Leitura de arquivo no qual cada elemento representa um Nodo do tipo funcionario
F1 = Funcionario("Ad01", "Joao", "eletronicos")
F2 = Funcionario("Ad02", "Maria", "eletronicos")
F3 = Funcionario("Ad03", "Jose", "eletronicos")
F4 = Funcionario("Ad04", "Lucas", "eletronicos")
F5 = Funcionario("Ad05", "Rodrigo", "eletronicos")

# chamada dos métodos pertencentes à Classe Lista que adiciona os funcionários
lista.NovoFuncionario(F1)
lista.NovoFuncionario(F2)
lista.NovoFuncionario(F3)
lista.NovoFuncionario(F4)
lista.NovoFuncionario(F5)

# chamada do método de impressão da Lista desenvolvida
lista.ImprimeLista()

# informa o número de funcionários
print("Total de funcionários na empresa: ",lista.Numero_Funcionarios())

# remove no meio da Lista
lista.Remove_Funcionario(F3)
lista.ImprimeLista()
print("Total de funcionários na empresa: ",lista.Numero_Funcionarios())

# remove no final da Lista
lista.Remove_Funcionario(F1)
lista.ImprimeLista()
print("Total de funcionários na empresa: ",lista.Numero_Funcionarios())

# remove no inicio da Lista
lista.Remove_Funcionario(F5)
lista.ImprimeLista()
print("Total de funcionários na empresa: ",lista.Numero_Funcionarios())