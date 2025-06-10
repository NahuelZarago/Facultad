#19. Dada una pila de películas de las que se conoce 
# su título, estudio cinematográfico y año de estreno
#desarrollar las funciones necesarias para 
#resolver las siguientes actividades:
#a.mostrar los nombre películas estrenadas 
#en el año 2014;
#b. indicar cuántas películas se estrenaron en el año 
#2018;
#c. mostrar las películas de Marvel Studios estrenadas 
#en el año 2016.
import stack

class Pelicula:
    def __init__(self, titulo: str, estudio: str, año: int):
        self.titulo = titulo
        self.estudio = estudio
        self.año = año

    def __str__(self):
        return f"{self.titulo} - {self.estudio} - {self.año}"

peliculas = stack.Stack()
peliculas.push(Pelicula("The Godfather", "Paramount Pictures", 1972))
peliculas.push(Pelicula("Guardians of the Galaxy", "Marvel Studios", 2014))
peliculas.push(Pelicula("Black Panther", "Marvel Studios", 2018))
peliculas.push(Pelicula("Captain America: Civil War", "Marvel Studios", 2016))
peliculas.push(Pelicula("Avengers: Infinity War", "Marvel Studios", 2018))
peliculas.push(Pelicula("Interstellar", "Paramount Pictures", 2014))

#a.mostrar los nombre películas estrenadas  en el año 2014;
def mostrar_nombres_peliculas(pila):
  aux = stack.Stack()
  while pila.size()>0:
    peli = pila.pop()
    if peli.año == 2014:
      print(peli.titulo)
    aux.push(peli)
  while aux.size() > 0:
    pila.push(aux.pop())

#b. indicar cuántas películas se estrenaron en el año 2018
def cuantas_peliculas(pila):
  aux = stack.Stack()
  contador = 0
  while pila.size()>0:
    peli = pila.pop()
    if peli.año ==2018:
      contador += 1
    aux.push(peli)
  while aux.size() > 0:
        pila.push(aux.pop())
  return contador

#c.mostrar las películas de Marvel Studios estrenadas en el año 2016.
def mostrar_peliculas_marvel(pila):
  aux = stack.Stack()
  while pila.size()>0:
    peli = pila.pop()
    if peli.estudio == "Marvel Studios" and peli.año == 2016:
        print(peli)
    aux.push(peli)
  while aux.size() > 0:
        pila.push(aux.pop())      

print("Peliculas estrenadas en 2014:")
mostrar_nombres_peliculas(peliculas)

print("Cantidad de peliculas estrenadas en 2018:", cuantas_peliculas(peliculas))

print("Peliculas de Marvel Studios estrenadas en 2016:")
mostrar_peliculas_marvel(peliculas)
