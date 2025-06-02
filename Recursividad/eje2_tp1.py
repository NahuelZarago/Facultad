num = int(input("Ingrese un numero positivo: "))

def enteros(n):
  suma = 0
  for i in range(n + 1):
    suma = suma + i
    return suma
print("La suma desde 0 hasta", num, "es:", enteros(num))
