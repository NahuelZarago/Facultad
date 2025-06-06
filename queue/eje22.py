#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU),
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe 
#y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, 
# {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
#desarrollar un algoritmo que resuelva las siguientes actividades:
#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar 
# su nombre de superhéroes.

import queue_

class Personaje:
    def __init__(self, nombre_personaje, nombre_heroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_heroe = nombre_heroe
        self.genero = genero

    def __str__(self):
        return f"{self.nombre_personaje} / {self.nombre_heroe} / {self.genero}"


personajes_data = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Stephen Strange", "Doctor Strange", "M"),
    ("Shuri", "Black Panther", "F"),
]


cola_personajes = queue.Queue()

for nombre_personaje, nombre_heroe, genero in personajes_data:
    cola_personajes.arrive(Personaje(nombre_personaje, nombre_heroe, genero))


def mostrar_cola(cola: queue.Queue):
    size = cola.size()
    for i in range(size):
        item = cola.on_front()
        print(item)
        cola.move_to_end()
    print()

#a 
def nombre_personaje_capitana_marvel(cola: queue.Queue):
    size = cola.size()
    for i in range(size):
        item = cola.on_front()
        if item.nombre_heroe == "Capitana Marvel":
            print(f"Personaje de Capitana Marvel: {item.nombre_personaje}")
        cola.move_to_end()

#b
def mostrar_heroes_femeninos(cola: queue.Queue):
    print("Superheroes femeninos:")
    size = cola.size()
    for i in range(size):
        item = cola.on_front()
        if item.genero == "F":
            print(item.nombre_heroe)
        cola.move_to_end()
    print()

#c
def mostrar_personajes_masculinos(cola: queue.Queue):
    print("Personajes masculinos:")
    size = cola.size()
    for i in range(size):
        item = cola.on_front()
        if item.genero == "M":
            print(item.nombre_personaje)
        cola.move_to_end()
    print()

#d
def heroe_de_scott_lang(cola: queue.Queue):
    size = cola.size()
    for i in range(size):
        item = cola.on_front()
        if item.nombre_personaje == "Scott Lang":
            print(f"Superheroe de Scott Lang: {item.nombre_heroe}")
        cola.move_to_end()

#e
def mostrar_nombres_con_s(cola: queue.Queue):
    print("Personajes o héroes que empiezan con 'S':")
    size = cola.size()
    for i in range(size):
        item = cola.on_front()
        if item.nombre_personaje.startswith("S") or item.nombre_heroe.startswith("S"):
            print(item)
        cola.move_to_end()
    print()

#d
def buscar_carol_danvers(cola: queue.Queue):
    size = cola.size()
    encontrado = False
    for i in range(size):
        item = cola.on_front()
        if item.nombre_personaje == "Carol Danvers":
            print(f"Carol Danvers esta en la cola, su superheroe es: {item.nombre_heroe}")
            encontrado = True
        cola.move_to_end()
    if not encontrado:
        print("Carol Danvers no esta en la cola.")



mostrar_cola(cola_personajes)

nombre_personaje_capitana_marvel(cola_personajes)
mostrar_heroes_femeninos(cola_personajes)
mostrar_personajes_masculinos(cola_personajes)
heroe_de_scott_lang(cola_personajes)
mostrar_nombres_con_s(cola_personajes)
buscar_carol_danvers(cola_personajes)

