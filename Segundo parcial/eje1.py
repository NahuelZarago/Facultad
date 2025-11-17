# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre, número, tipo/tipos, debilidad frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool) para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
# los índices de cada uno de los árboles deben ser nombre, número y tipo;
# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
# mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
# realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
# mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
# mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
# determinar cuantos Pokémons tienen megaevolucion.
# determinar cuantos Pokémons tiene forma gigamax.
from queue_ import Queue
from tree import BinaryTree as Tree
from pokedex_data import pokedex 

#Creo la clase pokemon
class Pokemon:
    def __init__(self, nombre: str, numero: int, tipos, debilidades, mega: bool, gigamax: bool):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos            
        self.debilidades = debilidades
        self.mega = mega
        self.gigamax = gigamax

    def __str__(self):
        return (
            f"{self.numero} - {self.nombre}\n"
            f"Tipos: {self.tipos}\n"
            f"Debilidades: {self.debilidades}\n"
            f"Mega: {self.mega} | Gigamax: {self.gigamax}\n"
        )

# creo los tres árboles 
arbol_por_numero = Tree()
arbol_por_nombre = Tree()
arbol_por_tipo = Tree()

#cargmos los pokemons en los tres árboles
for p in pokedex:
    poke = Pokemon(
        p["nombre"],
        p["numero"],
        p["tipos"],
        p["debilidades"],
        p["mega"],
        p["gigamax"]
    )

    # índice por número
    arbol_por_numero.insert(poke.numero, poke)
    # índice por nombre 
    arbol_por_nombre.insert(poke.nombre.lower(), poke)
    # índice por tipo (uno por cada tipo que tenga)
    for t in poke.tipos:
        arbol_por_tipo.insert(t.lower(), poke)

# creamos esta funcion para buscar por numero 
def buscar_por_numero(n):
    nodo = arbol_por_numero.search(n)
    if nodo:
        print(nodo.other_values)  
    else:
        print("no existe ese pokemon.")
#ahora creo esta funcion para buscar por nombre fragmento
def buscar_por_nombre_fragmento(fragmento: str):
    fragmento = fragmento.lower()
    cola = Queue()

    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            if fragmento in root.value:
                cola.arrive(root.other_values)
            recorrer(root.right)

    recorrer(arbol_por_nombre.root)

    while cola.size() > 0:
        print(cola.attention())

#creo esta funcion para conseguir los pokemons por tipo
def pokemons_por_tipo(tipo: str):
    tipo = tipo.lower()
    cola = Queue()

    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            if root.value == tipo:
                cola.arrive(root.other_values)
            recorrer(root.right)

    recorrer(arbol_por_tipo.root)

    while cola.size() > 0:
        print(cola.attention().nombre)

# aca creo la funcion para listar por numero 
def listado_por_numero():
    arbol_por_numero.in_order()
# esta otra funcion es para listar por nombre
def listado_por_nombre():
    arbol_por_nombre.in_order()
# esta funcion es para listar por nivel por nombre
def listado_por_nivel_nombre():
    arbol_por_nombre.by_level()

# esta funcion es para poner los pokemons debiles a una lista de nombres
def debiles_a(lista_nombres):
    tipos_objetivo = set()
    for nombre in lista_nombres:
        nodo = arbol_por_nombre.search(nombre.lower())
        if nodo:
            poke = nodo.other_values
            # agrego todos los tipos del pokémon objetivo
            for t in poke.tipos:
                tipos_objetivo.add(t.lower())

    # recorro el árbol por número (o por nombre) y meto los los débiles
    cola = Queue()
    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            p = root.other_values
            # si alguna de las debilidades del pokémon coincide con tipos_objetivo
            if any(t.lower() in tipos_objetivo for t in p.debilidades):
                cola.arrive(p)
            recorrer(root.right)

    recorrer(arbol_por_numero.root)

    # imprimo sin repetir (uso un set para nombres ya vistos)
    vistos = set()
    while cola.size() > 0:
        p = cola.attention()
        if p.nombre not in vistos:
            print(p.nombre)
            vistos.add(p.nombre)

#en esta funcion mostramos todos los tipos y cuantos hay de cada tipo
def contar_por_tipo():
    tipos = {}

    # Recorro el arbol por tipo y cuento
    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            p = root.other_values
            for t in p.tipos:
                key = t.lower()
                tipos[key] = tipos.get(key, 0) + 1
            recorrer(root.right)

    recorrer(arbol_por_numero.root)

    for t, c in tipos.items():
        print(f"{t}: {c}")

# y por ultimo esta funcion cuenta cuantos pokemons tienen mega evolucion y cuantos gigamax
def contar_mega_giga():
    mega = 0
    giga = 0

    def recorrer(root):
        nonlocal mega, giga
        if root is not None:
            recorrer(root.left)
            p = root.other_values
            if p.mega:
                mega += 1
            if p.gigamax:
                giga += 1
            recorrer(root.right)

    recorrer(arbol_por_numero.root)

    print("pokemon con megaevolucion:", mega)
    print("pokemon con gigamax:", giga)


if __name__ == "__main__":
    print("Buscar por numero (6):")
    buscar_por_numero(6)

    print("Buscar por nombre fragmento 'bul':")
    buscar_por_nombre_fragmento("bul")

    print("Pokemons tipo Fuego:")
    pokemons_por_tipo("Fire")  

    print("Listado por numero ( usando in_order):")
    listado_por_numero()

    print("Listado por nombre ( usando in_order):")
    listado_por_nombre()

    print("Listado por niveles (por nombre):")
    listado_por_nivel_nombre()

    print("Pokemons debiles a Jolteon, Lycanroc, Tyrantrum:")
    debiles_a(["Jolteon", "Lycanroc", "Tyrantrum"])

    print("Conteo por tipo:")
    contar_por_tipo()

    print("Mega / Gigamax contacion:")
    contar_mega_giga()
