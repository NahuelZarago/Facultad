#2. Utilizando operaciones de cola y pila, invertir el contenido de una cola.
from queue_ import Queue
from stack import Stack

cola = Queue()
cola.arrive(5)
cola.arrive(52)
cola.arrive(12)
cola.arrive(32)
cola.arrive(4554)
cola.arrive(777)

print('cola original:')
cola.show()
def InvertirContenidoColaConPila(cola):
    pila = Stack()
    while cola.size() > 0:
        pila.push(cola.attention())
    
    while pila.size() > 0:
        cola.arrive(pila.pop())
    print('cola invertida:')  
    cola.show()



InvertirContenidoColaConPila(cola)
