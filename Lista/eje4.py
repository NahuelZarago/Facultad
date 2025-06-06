# 4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.

from list_ import List

lista = List()

lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)


def addition(lista,position,number):
    if position < 0 or position > len(lista):
        print("Error")
    else:
        lista.insert(position, number)


addition(lista, 4, 9)
addition(lista, 6, 10)

print(lista.show())   
