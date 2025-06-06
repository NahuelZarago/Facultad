#1. Eliminar de una cola de caracteres todas las vocales que aparecen.
import queue_

cola = queue_.Queue()
caracteres = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

for i in caracteres:
  cola.arrive(i)
  
print('Cola original:')
cola.show()
 
def eliminar_vocales(cola):
  aux = queue_.Queue()
  vocales = "aeiouAEIOU"
  while cola.size() > 0:
    caracter = cola.attention()
    if caracter not in vocales:
      aux.arrive(caracter)
  while aux.size() > 0:
    cola.arrive(aux.attention())

print("cola sin las vocales:")
eliminar_vocales(cola)
cola.show
