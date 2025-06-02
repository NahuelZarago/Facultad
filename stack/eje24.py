#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

import stack

class Personaje:
    def __init__(self, nombre: str, peliculas: int):
        self.nombre = nombre
        self.peliculas = peliculas

    def __str__(self):
        return f"{self.nombre} - {self.peliculas} peliculas"


pila_marvel = stack.Stack()
personajes = [
    ("Iron Man", 10),
    ("Black Widow", 8),
    ("Hulk", 7),
    ("Captain America", 9),
    ("Groot", 5),
    ("Rocket Raccoon", 6),
    ("Doctor Strange", 4),
    ("Gamora", 6),
    ("Drax", 6),
    ("Captain Marvel", 3),
]

for nombre, pelis in personajes:
    pila_marvel.push(Personaje(nombre, pelis))

#a
def posicion_personajes(pila):
    aux = stack.Stack()
    posiciones = {}
    pos_actual = 1

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje.nombre in ["Rocket Raccoon", "Groot"]:
            posiciones[personaje.nombre] = pos_actual
        aux.push(personaje)
        pos_actual += 1

    while aux.size() > 0:
        pila.push(aux.pop())

    for nombre in ["Rocket Raccoon", "Groot"]:
        if nombre in posiciones:
            print(f"{nombre} esta en la posicion {posiciones[nombre]} desde la cima.")
        else:
            print(f"{nombre} no esta en la pila.")

#b
def personajes_mas_de_5(pila):
    aux = stack.Stack()
    print("Personajes con mas de 5 peliculas:")
    while pila.size() > 0:
        p = pila.pop()
        if p.peliculas > 5:
            print(f"{p.nombre} ({p.peliculas} peliculas)")
        aux.push(p)
    while aux.size() > 0:
        pila.push(aux.pop())

#c
def peliculas_black_widow(pila):
    aux = stack.Stack()
    encontrada = False
    while pila.size() > 0:
        p = pila.pop()
        if p.nombre == "Black Widow":
            print(f"Black Widow participo en {p.peliculas} peliculas.")
            encontrada = True
        aux.push(p)
    while aux.size() > 0:
        pila.push(aux.pop())
    if not encontrada:
        print("Black Widow no esta en la pila.")

#d
def personajes_por_letra(pila):
    aux = stack.Stack()
    print("Personajes que empiezan con C, D o G:")
    while pila.size() > 0:
        p = pila.pop()
        if p.nombre[0] in ["C", "D", "G"]:
            print(f"{p.nombre}")
        aux.push(p)
    while aux.size() > 0:
        pila.push(aux.pop())

# 
posicion_personajes(pila_marvel)
personajes_mas_de_5(pila_marvel)
peliculas_black_widow(pila_marvel)
personajes_por_letra(pila_marvel)
