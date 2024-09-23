#Lista de sobremesas
doces = ['pudim','bombom','chocolate']

#Lista de valores
valores = [2,5,1,10,5]

#Impressão das listas
print('listas originais')
print(doces)
print(valores)

#Adicionar elementos
doces.append('cocada')
valores.insert(1,50)
print('lista com novos elementos')
print(doces)
print(valores)

#Remover elementos
doces.remove('bombom')
valores.remove(1)
print('listas com a remoção de 1 elementos')
print(doces)
print(valores)