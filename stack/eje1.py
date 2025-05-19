import random

stack = []

for _ in range (10):
  numero = random.randint(1, 100)
  stack.append(numero)
print(stack)
print("El total de numeros dentro de la pila es de: " ,len(stack))
