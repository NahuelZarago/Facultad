#Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
#verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
#usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
#las siguientes actividades:
#a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
#además mostrar el nombre de dichas películas;
#b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
#c. eliminar los modelos de los trajes destruidos mostrando su nombre;
#d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
#más de un modelo de traje, estos deben cargarse por separado;
#e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
#repetidos en una misma película;
#f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
#“Capitan America: Civil War”.

import stack

class Armadura:
    def __init__(self, modelo: str, pelicula: str, estado: str):
        self.modelo = modelo
        self.pelicula = pelicula
        self.estado = estado

    def __str__(self):
        return f"{self.modelo} - {self.pelicula} - {self.estado}"

IronMan = stack.Stack()
datos = [
    ("Mark III", "Iron Man", "Dañado"),
    ("Mark XLIV", "Avengers: Age of Ultron", "Impecable"),
    ("Mark XLV", "Avengers: Age of Ultron", "Destruido"),
    ("Mark XLVI", "Captain America: Civil War", "Dañado"),
    ("Mark XLVII", "Spider-Man: Homecoming", "Impecable"),
    ("Mark L", "Avengers: Infinity War", "Destruido"),
    ("Mark LXXXV", "Avengers: Endgame", "Dañado"),
]

for modelo, pelicula, estado in datos:
    IronMan.push(Armadura(modelo, pelicula, estado))

#a
def modelo_mark(pila: stack.Stack):
    aux = stack.Stack()
    peliculas = []

    while pila.size() > 0:   #traje es una variable temporal para almacenar el elemento que se saca de la pila (le llamo traje a la armadura)
        traje = pila.pop()  
        if traje.modelo == "Mark XLIV":
            peliculas.append(traje.pelicula)
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())  #reestablecemos la pila a exactamente como estaba 

    if peliculas:
        print("Mark XLIV fue utilizada en:")
        for peli in peliculas:
            print(f"{peli}")
    else:
        print("Mark XLIV no fue utilizada en ninguna pelicula.")

#b
def mostrar_dañados(pila: stack.Stack):
    aux = stack.Stack()
    dañados = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje.estado == "Dañado":
            dañados.append(f"{traje.modelo} ({traje.pelicula})")
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    print("Modelos dañados:")
    for d in dañados:
        print(f"{d}")

#c
def eliminar_destruidos(pila: stack.Stack):
    aux = stack.Stack()
    print("Modelos destruidos eliminados:")

    while pila.size() > 0:
        traje = pila.pop()
        if traje.estado == "Destruido":
            print(f"{traje.modelo} ({traje.pelicula})")
        else:
            aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

#e
def agregar_traje(pila: stack.Stack, modelo: str, pelicula: str, estado: str):
    aux = stack.Stack()
    existe = False

    while pila.size() > 0:
        traje = pila.pop()
        if traje.modelo == modelo and traje.pelicula == pelicula:
            existe = True
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if existe:
        print(f"No se puede agregar: {modelo} porque ya se encuentra en {pelicula}")
    else:
        pila.push(Armadura(modelo, pelicula, estado))
        print(f"{modelo} se agrego en {pelicula}")

#f
def mostrar_trajes_por_pelicula(pila: stack.Stack, peliculas_objetivo: list):
    aux = stack.Stack()
    print("Trajes usados en las peliculas indicadas:")

    while pila.size() > 0:
        traje = pila.pop()
        if traje.pelicula in peliculas_objetivo:
            print(f"{traje.modelo} en {traje.pelicula}")
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

modelo_mark(IronMan)
mostrar_dañados(IronMan)
eliminar_destruidos(IronMan)
agregar_traje(IronMan, "Mark LXXXV", "Avengers: Endgame", "Dañado")
mostrar_trajes_por_pelicula(IronMan, ["Spider-Man: Homecoming", "Captain America: Civil War"])
