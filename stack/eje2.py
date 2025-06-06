#Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
#meros pares.
import stack
import random

pilas = stack.Stack()
for i in range(10):
    pilas.push(random.randint(1, 100))

print("Pila original: ")
pilas.show()

def eliminar_impares(pila):
    aux = stack.Stack()
    while pila.size() > 0:
        valor = pila.pop()
        if valor % 2 == 0:
            aux.push(valor)

    while aux.size() > 0:
        pila.push(aux.pop())

print("Pila sin impares:")
eliminar_impares(pilas)
pilas.show()
