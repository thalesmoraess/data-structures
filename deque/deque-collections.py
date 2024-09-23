# vamos criar uma deque e aplicar as operações disponíveis por meio do uso da biblioteca COLLECTIONS.

import collections
d = collections.deque()
print (d)

# agora, vamos adicionar dois elementos na sequência, “a” e “b”, que serão inseridos à direita da deque
d.append('a')
d.append('b')
print(d)

# adicionaremos mais um elemento “b”, agora à esquerda
d.appendleft('b')
print (d)

# agora, vamos inserir à direita diversos elementos
d.extend('cdef')
print(d)

# também vamos inserir mais de um elemento à esquerda
d.extendleft('ghij')
print(d)

# inserimos o elemento “k” na posição 5
d.insert(5, 'k')
print(d)

# removemos o elemento à direita, que no caso será o “f”
d.pop()
print(d)

# removemos o elemento à esquerda, que no caso será o “j”
d.popleft()
print(d)

# removemos, especificamente, a primeira ocorrência do elemento “b”
d.remove('b')
print(d)

# invertemos a deque utilizando o comando "reverse"
d.reverse()
print(d)

# limpamos a deque, excluindo todos os elementos
d.clear()
print(d)

# adicionalmente, também é possível criar uma deque com tamanho definido. No exemplo, limitamos o tamanho a 30 elementos:
d3 = collections.deque(maxlen=30)
print(d3)