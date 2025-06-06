#1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
from list_ import List

lista = List()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

def contadordenodos(value):
    return len(value)

print(f"hay {contadordenodos(lista)} nodos en la lista")
