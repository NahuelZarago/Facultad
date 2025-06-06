#Dada una lista de números enteros eliminar de estas los números primos.
from list_ import List

lista = List()

lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(7)
lista.append(8)

def remove_primo(value):
    for lista in value[:]:
        if lista % 2 != 0 and lista > 1:
            value.remove(lista)

print('Lista sin los numeros primos:')
remove_primo
print(lista.show())
