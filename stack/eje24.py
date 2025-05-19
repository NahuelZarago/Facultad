#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

pila = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Black Widow", "peliculas": 8},
    {"nombre": "Hulk", "peliculas": 7},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Groot", "peliculas": 5},
    {"nombre": "Rocket Raccoon", "peliculas": 6},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Gamora", "peliculas": 6},
    {"nombre": "Drax", "peliculas": 6},
    {"nombre": "Captain Marvel", "peliculas": 3},
]

#a
def posicionpersonajes(pila):
    personajes_buscados = ["Rocket Raccoon", "Groot"]
    for nombre in personajes_buscados:
        posicion = None
        for i in range(len(pila)-1, -1, -1):  
            if pila[i]["nombre"] == nombre:
                posicion = len(pila) - i  
        if posicion is not None:
            print(f"{nombre} esta en la posicion {posicion} desde la cima")
        else:
            print(f"{nombre} no esta en la pila")
#b
def personajes_mas_de_5(pila):
    print("personajes con mas de 5 peliculas:")
    for p in pila:
        if p["peliculas"] > 5:
            print(f"{p['nombre']} ({p['peliculas']} peliculas)")
            
            
#c
def peliculas_black_widow(pila):
    for p in pila:
        if p["nombre"] == "Black Widow":
            print(f"Black Widow participo en {p['peliculas']} peliculas")
            return
    print("Black Widow no esta en la pila")
    
#d
def personajes_por_letra(pila):
    print("Personajes que empiezan con C, D o G:")
    for p in pila:
        if p["nombre"][0] in ["C", "D", "G"]:
            print(f"{p['nombre']}")

posicionpersonajes(pila)
personajes_mas_de_5(pila)
peliculas_black_widow(pila)
personajes_por_letra(pila)
