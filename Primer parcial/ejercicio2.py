#Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) 
#debe tener 100 o mas, resolver:
#A.Listado ordenado de manera ascendente por nombre de los personajes.
#B.Determinar en que posicion esta The Thing y Rocket Raccoon.
#C.Listar todos los villanos de la lista.
#D.Poner todos los villanos en una cola para determinar luego cuales 
#aparecieron antes de 1980.
#E.Listar los superheores que comienzan con  Bl, G, My, y W.
#F.Listado de personajes ordenado por nombre real de manera ascendente de 
#los personajes.
#G.Listado de superheroes ordenados por fecha de aparación.
#H.Modificar el nombre real de Ant Man a Scott Lang.
#I.Mostrar los personajes que en su biografia incluyan la palabra time-traveling 
#o suit.
#J.Eliminar a Electro y Baron Zemo de la lista y mostrar su información si 
#estaba en la lista


from super_heroes_data import superheroes
from queue_ import Queue
from list_ import List

class Personaje:
    def __init__(self, nombre, nombre_real, genero, villano, fecha_aparicion, biografia):
        self.nombre = nombre
        self.nombre_real = nombre_real
        self.genero = genero
        self.villano = villano
        self.fecha_aparicion = int(fecha_aparicion)
        self.biografia = biografia

    def __str__(self):
        return f"{self.nombre} / {self.nombre_real} / {self.genero} / {self.villano} / {self.fecha_aparicion}"


# Funciones de criterio 
def criterio_nombre(personaje):
    return str(personaje.nombre)

def criterio_nombre_real(personaje):
    return str(personaje.nombre_real)

def criterio_fecha_aparicion(personaje):
    return int(personaje.fecha_aparicion)


lista = List()
for i in superheroes:
    personaje = Personaje(
        nombre=i["alias"],
        nombre_real=i["real_name"],
        genero="desconocido",
        villano=i["is_villain"],
        fecha_aparicion=i["first_appearance"],
        biografia=i["short_bio"]
    )
    lista.append(personaje)

#agrego los criterios
lista.add_criterion("nombre", criterio_nombre)
lista.add_criterion("nombre_real", criterio_nombre_real)
lista.add_criterion("fecha_aparicion", criterio_fecha_aparicion)


# A. Listado ordenado por nombre real
def listado_ordenado(lista):
    lista.sort_by_criterion("nombre_real")
    lista.show()

# B. Buscar posiciones
def determinar_posicion(lista):
    pos1 = lista.search("the thing", "nombre")
    pos2 = lista.search("rocket raccoon", "nombre")
    print(f"The Thing está en la posición: {pos1}")
    print(f"Rocket Raccoon está en la posición: {pos2}")

# C. Listar todos los villanos
def listar_villanos(lista):
    villanos = [p for p in lista if p.villano]
    if villanos:
        for v in villanos:
            print(v)
    else:
        print("No hay villanos en la lista")

# D. Cola de villanos antes de 1980
def cola_villanos_antes_1980(lista):
    cola = Queue()
    for personaje in lista:
        if personaje.villano and personaje.fecha_aparicion < 1980:
            cola.arrive(personaje)
    return cola

def mostrar_cola(cola):
    if cola.size() == 0:
        print("No hay villanos en la cola")
    else:
        print("Villanos que aparecieron antes de 1980:")
        while cola.size() > 0:
            print(cola.attention())

# E. Superheroes que comienzan con Bl, G, My, W
def listar_superheroes(lista):
    iniciales = ("bl", "g", "my", "w")
    encontrados = False
    for personaje in lista:
        if personaje.nombre.lower().startswith(iniciales):
            print(personaje)
            encontrados = True
    if not encontrados:
        print("No se encontraron superheroes que comiencen con esas iniciales")

# F. Ordenado por nombre real
def listado_personajes(lista):
    lista.sort_by_criterion("nombre_real")
    lista.show()

# G. Ordenado por fecha de aparicion
def superheroes_ordenados(lista):
    lista.sort_by_criterion("fecha_aparicion")
    lista.show()

# H. Modificar nombre real de Ant Man a Scott Lang
def modificar_nombre(lista):
    pos = lista.search("ant man", "nombre")
    if pos is not None:
        lista[pos].nombre_real = "Scott Lang"
        print("Modificado:", lista[pos])
    else:
        print("Ant Man no se encuentra en la lista")

# I. Mostrar personajes con "time-traveling" o "suit"
def mostrar_personajes(lista):
    encontrados = False
    for personaje in lista:
        bio = personaje.biografia.lower()
        if 'time-traveling' in bio or 'suit' in bio:
            print(personaje)
            encontrados = True
    if not encontrados:
        print("No se encontraron personajes con esas palabras clave")

# J. Eliminar Electro y Baron Zemo
def eliminar_electro_baron(lista):
    electro = lista.delete_value("electro", "nombre")
    zemo = lista.delete_value("baron zemo", "nombre")
    if electro:
        print("Electro eliminado:", electro)
    else:
        print("Electro no estaba en la lista")
    if zemo:
        print("Baron Zemo eliminado:", zemo)
    else:
        print("Baron Zemo no estaba en la lista")


# Ejecutar todos los puntos
print("A. Listado ordenado de manera ascendente por nombre de los personajes:")
listado_ordenado(lista)

print("B. Determinar en que posicion esta The Thing y Rocket Raccoon:")
determinar_posicion(lista)

print("C. Listar todos los villanos de la lista:")
listar_villanos(lista)

print("D. Todos los villanos en una cola que aparecieron antes de 1980:")
cola = cola_villanos_antes_1980(lista)
mostrar_cola(cola)

print("E. Superheroes que comienzan con Bl, G, My, y W:")
listar_superheroes(lista)

print("F. Listado de personajes ordenado por nombre real:")
listado_personajes(lista)

print("G. Listado de superheroes ordenado por fecha de aparicion:")
superheroes_ordenados(lista)

print("H. Modificar el nombre real de Ant Man a Scott Lang:")
modificar_nombre(lista)

print("I. Personajes con 'time-traveling' o 'suit' en la biografia:")
mostrar_personajes(lista)

print("J. Eliminar a Electro y Baron Zemo de la lista:")
eliminar_electro_baron(lista)
