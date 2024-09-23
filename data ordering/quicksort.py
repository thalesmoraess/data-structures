import random

def partition(seq, low, high):
    pivot_index = random.randint(low, high -1) # escolhe um íncice aleatório como pivot
    pivot = seq[pivot_index] # valor do pivot
    seq[pivot_index], seq[high - 1], = seq[high - 1], seq[pivot_index] # move o pivot para o final
    i = low # índice do elemento menor encontrado
    for j in range(low, high - 1):
        if seq[j] < pivot:
            seq[i], seq[j] = seq[j], seq[i] # troca os elementos menores para a esquerda do pivot
            i += 1
    seq[i], seq[high - 1] = seq[high - 1], seq[i] # coloca o pivot em sua posição correta
    return i

def quicksort(seq):
    quicksort_helper(seq, 0, len(seq)) # chama a função auxiliar para ordenar toda a lista

def quicksort_helper(seq, low, high):
    if low < high - 1:
        pivot_index = partition(seq, low, high) # realiza o particionamento
        quicksort_helper(seq, low, pivot_index) # ordena a sublista à esquerda do pivot
        quicksort_helper(seq, pivot_index + 1, high) # ordena a sublista à direita do pivot

# exemplo de uso
numbers = [5, 8, 2, 6, 9, 1, 0, 7]
quicksort(numbers) # chama a função para ordenar a lista
print(numbers)