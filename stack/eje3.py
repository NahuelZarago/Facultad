#Reemplazar todas las ocurrencias de un determinado elemento en una pila.

pila = [1, 2, 4, 8, 1, 7, 1, 1]
print("Pila original: ", pila)

reemplazar = 1
nuevo = 0

aux = []

while pila:
  if pila.pop() == reemplazar:
    aux.append(nuevo)
  else:
    aux.append(pila.pop())

while aux:
  pila.append(aux.pop())
print("Pila modificada: ",pila) 
