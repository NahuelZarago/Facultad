num = int(input("Pone cualquier numero: "))

def fibo(n):
  #(Para ayudarme) si n vale 0 entonces devolverá 0 pero si vale 1 entonces devolverá 1
  if n == 0:
    return 0
  if n == 1:
    return 1
  else:
    a = 0
    b = 1
    for i in range(2, n + 1):
      temp = a + b
      a = b
      b = temp
    return b
  
print("El valor de Fibonacci en la posicion", num, "es:", fibo(num))
