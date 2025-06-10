#Implementar una función que permita obtener el valor 
#en la sucesión de Fibonacci para un  
#número dado de forma recursiva.

def fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def mostrar_fibonacci(n):
    for i in range(n):
        print(fibonacci(i))

mostrar_fibonacci(10)
