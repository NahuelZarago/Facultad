#4. Dada una cola de números cargados aleatoriamente, 
#eliminar de ella todos los que no sean primos.
import random
from queue_ import Queue
from stack import Stack

def es_primo(n):
  if n<2:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
    return True

cola = Queue()
for i in range(10):
  cola.arrive(random.randint(1,100))
  
print("Cola original:")
cola.show()
  
def dejar_solo_primos(cola):
 tamaño = cola.size()
 for i in range(tamaño):
    num = cola.attention()
    if es_primo(num):
     cola.arrive(num)
     
dejar_solo_primos(cola) 
print("la cola solo con primos:")
cola.show()

