#7. Implementar los algoritmos necesarios para resolver las siguientes tareas:
#a. concatenar dos listas, una atrás de la otra;
#b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
#c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;
#d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido.
from list_ import List

#a
lista_1 = List([1, 2, 3])
lista_2 = List([4, 5, 6])

lista_enlazada = lista_1 + lista_2  
print("lista unida :", lista_enlazada)

#b
def concatenar_sin_repetidos(l1, l2):
    resultado = List()
    vistos = set()
    for elem in l1 + l2:
        if elem not in vistos:
            vistos.add(elem)
            resultado.append(elem)
    return resultado

lista_sin_repetidos = concatenar_sin_repetidos(lista_1, lista_2)
print("Concatenación sin repetidos:", lista_sin_repetidos)



#c
def contar_repetidos(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    interseccion = set1.intersection(set2)
    return len(interseccion)
print("Cantidad de elementos repetidos:", contar_repetidos(lista_1, lista_2))

#d
def eliminar_mostrar(lista):
    while lista:
        eliminado = lista.pop(0)
        print("Eliminado:", eliminado)

print("Eliminando elementos de lista_1:")
eliminar_mostrar(lista_1)
print("Lista 1 ahora:", lista_1)
