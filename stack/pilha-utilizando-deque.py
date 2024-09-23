# Programa em Python para
# demonstrar a implementação de pilha
# utilizando a coleção .deque
from collections import deque
stack = deque()

# função append() para inserir
# elementos na pilha
stack.append('a')
stack.append('b')
stack.append('c')
print('Pilha inicial:')
print(stack)

# função pop() para remover
# elementos da pilha
# na ordem LIFO
print('\nElementos removidos da pilha:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nPilha após retirada dos elementos:')
print(stack)
# O uso de print(stack.pop())
# causará o erro IndexError
# devido à pilha estar vazia agora.