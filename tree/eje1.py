# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:

# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.


from tree import BinaryTree
import random


arbol = BinaryTree()  #Para crear el arbol


for _ in range(1000):
    numero = random.randint(0, 500)
    arbol.insert(numero)

#a
print("Recorrido Preorden:")
arbol.pre_order()

print("Recorrido Inorden:")
arbol.in_order()

print("Recorrido Postorden:")
arbol.post_order()

print("Recorrido por Nivel:")
arbol.by_level()

# b
buscado = 250
pos = arbol.search(buscado)
if pos:
    print(f"El numero {buscado} esta en el arbol")
else:
    print(f"El numero {buscado} no esta en el arbol")

# c
for valor in [100, 200, 300]:
    arbol.delete(valor)
    print(f"Se elimin el valor {valor} (si existia)")

# d
print("Altura subarbol izquierdo:", arbol.root.left.height if arbol.root.left else 0)
print("Altura subarbol derecho:", arbol.root.right.height if arbol.root.right else 0)

# e
buscado = 150
pos = arbol.search(buscado)
if pos:
    print(f"El numero {buscado} aparece {pos.other_values['count']} veces en el arbola")
else:
    print(f"El numero {buscado} no esta en el arbol")

# f
pares = 0
impares = 0

def contar_pares_impares(node):
    global pares, impares
    if node:
        if node.value % 2 == 0:
            pares += node.other_values['count']
        else:
            impares += node.other_values['count']
        contar_pares_impares(node.left)
        contar_pares_impares(node.right)

contar_pares_impares(arbol.root)

print(f"Cantidad de numeros pares: {pares}")
print(f"Cantidad de numeros impares: {impares}")
