#Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
#meros pares.

import random

pila = [random.randint(1, 100) for _ in range(10)]
print("Pila original: ", pila)
Parpila = []

while pila:
  sacar = pila.pop()
  if sacar % 2 == 0:
    Parpila.append(sacar)
    
while Parpila:
  pila.append(Parpila.pop())
  print(pila)
