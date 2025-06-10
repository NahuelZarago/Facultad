#Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes 
#realizar dos funciones recursivas:
#funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
#funcion recursiva para listar los superheroes de la lista.

superheroes = [
    "Iron Man", "Hulk", "Thor", "Black Widow", "Hawkeye",
    "Spiderman", "Doctor Strange", "Black Panther", "Robin", "Wasp",
    "Falcon", "Winter Soldier", "Scarlet Witch", "Vision", "Capitan America"
]

#Funcion recursiva
def recursiva(lista):
  if not lista:
      return False
  if lista[0] == "Capitan America":
      return True
  return recursiva(lista[1:]) #verificara si al recorrer toda la lista se encuentra capitan america, si eso es verdad, devolvera true, si no lo es, devolvera false

#Listar superheroes 
def listar_superheroes(lista):
  if not lista:
    return 
  print(lista[0])
  listar_superheroes(lista[1:]) #si la lista no esta vacia que te enliste desde el primero en la lista hasta el ultimo
  
print("Verificar si se encuentra Capitan America:")
print(recursiva(superheroes))
print("Listado de superheroes:")
listar_superheroes(superheroes)
