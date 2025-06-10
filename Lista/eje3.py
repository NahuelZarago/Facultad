# Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
# una que contenga los números pares y otra para los números impares.
from list_ import List  

lista = List()
lista.append(2)
lista.append(3)
lista.append(6)
lista.append(5)
x
def dividir(lista):
    pares_lista = []
    impares_lista = []

    for num in lista.show():  
        if num % 2 == 0:
            pares_lista.append(num)
        else:
            impares_lista.append(num)
    
    return pares_lista, impares_lista

pares, impares = dividir(lista)

print('Lista de numeros pares: ', pares)
print('Lista de numeros impares: ', impares)
print('lista original:', lista.show())
