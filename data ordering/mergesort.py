# observe no código a seguir como funciona o algoritmo Mergesort, realizando a classificação do conjunto de entrada 35, 78, 60, 24, 15, 3, 57, 101:
def merge(seq, start, mid, stop):
    lst = []
    i = start
    j = mid
    # mescla as duas listas enquanto cada uma tiver mais elementos
    while i < mid and j < stop:
        if seq[i] < seq[j]:
            lst.append(seq[i])
            i += 1
        else:
            lst.append(seq[j])
            j += 1
    # copia o restante da sequência do início ao meio
    while i < mid:
        lst.append(seq[i])
        i += 1
    # copia o resto da sequência do meio até o fim (não é obrigatório)
    while j < stop:
        lst.append(seq[j])
        j += 1
    # copia os elementos de volta para a sequência original
    for i in range(len(lst)):
        seq[start + i] = lst[i]

def mergeSortRecursively(seq, start, stop):
    if start >= stop - 1:
        return
    mid = (start + stop) //2
    mergeSortRecursively(seq, start, mid)
    mergeSortRecursively(seq, mid, stop)
    merge(seq, start, mid, stop)

def mergeSort(seq):
    mergeSortRecursively(seq, 0, len(seq))

# exemplo de uso
numbers = [35, 78, 60, 24, 15, 3, 57, 101]
mergeSort(numbers)
print(numbers)