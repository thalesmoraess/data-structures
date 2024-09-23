# vamos, novamente, criar uma deque e iniciá-la, utilizando o comando "extend" que vimos anteriormente
import collections
d = collections.deque()
d.extend('abcdefgh')
print(d)

# usando o comando copy, vamos fazer uma cópia da versão atual da deque. Assim, quando criamos uma cópia e continuamos manipulando a versão original, a cópia mantém o estado do momento em que foi duplicada
d2 = d.copy()
print(d2)

# agora, vamos contar quantos elementos iguais a "b" há na deque
print(d.count('b'))

# agora, perguntamos à deque qual é o índice do elemento “a” (lembrando que o índice do primeiro elemento é igual a zero)
print(d.index('a'))