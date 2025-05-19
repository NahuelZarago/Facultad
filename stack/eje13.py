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

pila_trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Impecable"},
    {"modelo": "Mark XLV", "pelicula": "Avengers: Age of Ultron", "estado": "Destruido"},
    {"modelo": "Mark XLVI", "pelicula": "Captain America: Civil War", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Dañado"},
]

#a
def modelo_mark(pila):
    peliculas = []
    for traje in pila:
        if traje["modelo"] == "Mark XLIV":
            peliculas.append(traje["pelicula"])
    if peliculas:
        print(f'Mark XLIV fue usada en: {peliculas}')
    else:
        print('Mark XLIV no fue usada en ninguna película.')

#b 
def dañados(pila):
    dañaditos = []
    for traje in pila:
        if traje["estado"] == "Dañado":
            dañaditos.append(f"{traje['modelo']} ({traje['pelicula']})")
    print("Los modelos dañados son:")
    for item in dañaditos:
        print(f"- {item}")

#c
def eliminar_destruidos(pila):
    nueva_pila = []
    print("Modelos destruidos eliminados:")
    for traje in pila:
        if traje["estado"] == "Destruido":
            print(f"- {traje['modelo']} ({traje['pelicula']})")
        else:
            nueva_pila.append(traje)
    return nueva_pila

#e
def agregar_traje(pila, modelo, pelicula, estado):
    for traje in pila:
        if traje["modelo"] == modelo and traje["pelicula"] == pelicula:
            print(f"No se puede agregar: {modelo} ya se encuentra en {pelicula}")
            return
    pila.append({"modelo": modelo, "pelicula": pelicula, "estado": estado})
    print(f"{modelo} se agrego en {pelicula}")

#f
def mostrar_trajes_por_pelicula(pila, peliculas):
    print("Trajes usados en las peliculas indicadas:")
    for traje in pila:
        if traje["pelicula"] in peliculas:
            print(f"- {traje['modelo']} en {traje['pelicula']}")
