# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas:
# cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# indicar qué personajes aparecieron en los nueve episodios de la saga.
from graph import Graph


# creo el grafo no dirigido para los personajes
g = Graph(is_directed=False)

personajes = [
    "Rey", "Han Solo", "C-3PO", "Chewbacca", "Leia",
    "Kylo Ren", "R2-D2", "Yoda", "Darth Vader",
    "Luke Skywalker", "BB-8", "Boba Fett"
]
# inserto los vértices en el grafo de personajes
for p in personajes:
    g.insert_vertex(p)


# inserto las aristas con la cantidad de episodios compartidos
aristas = [
    ("Luke Skywalker", "Leia", 6),
    ("C-3PO", "Han Solo", 4),
    ("Han Solo", "Chewbacca", 9),
    ("Yoda", "C-3PO", 2),
    ("C-3PO", "R2-D2", 9),
    ("Rey", "Kylo Ren", 3),
    ("Luke Skywalker", "Yoda", 3),
    ("Leia", "Darth Vader", 4),
    ("BB-8", "R2-D2", 1),
    ("Luke Skywalker", "Han Solo", 5),

    ("Rey", "BB-8", 3),
    ("Han Solo", "Kylo Ren", 1),
    ("Luke Skywalker", "Darth Vader", 4),
    ("Rey", "Yoda", 1),
    ("C-3PO", "Leia", 7),

    ("Kylo Ren", "Darth Vader", 2),
    ("Luke Skywalker", "R2-D2", 7),
    ("Han Solo", "Leia", 6),
    ("Yoda", "Luke Skywalker", 3),
    ("Rey", "Kylo Ren", 3),   
]

#inserto las aristas en el grafo de personajes
for o, d, w in aristas:
    g.insert_edge(o, d, w)

#creo la funcion desde arbol minimo para conseguir el arbol de expansion minimo
def arbol_expansion_minimo(grafo, inicio):
    min = grafo.kruskal(inicio)
    partes = min.split(";")
    arbol = []
    peso_total = 0
    for tramo in partes:
        datos = tramo.split("-")
        if len(datos) == 3:
            o, d, w = datos
            arbol.append((o, d, int(w)))
            peso_total += int(w)

    return peso_total, arbol

# creo la funcion para conseguir la relacion maxima entre personajes
def relacion_maxima(grafo):
    mayor = 0
    pares = []
    for v in grafo:
        for e in v.edges:
            if e.weight > mayor:
                mayor = e.weight
                pares = [(v.value, e.value)]
            elif e.weight == mayor:
                pares.append((v.value, e.value))

    return mayor, pares

# creo la funcion para conseguir el camino minimo entre dos personajes
def camino_min(grafo, origen, destino):

    pila = grafo.dijkstra(origen)
    ruta = []
    costo = None
    actual = destino

    while pila.size() > 0:
        nodo, dist, previo = pila.pop()
        if nodo == actual:
            if costo is None:
                costo = dist
            ruta.append(nodo)
            actual = previo

    ruta.reverse()

    return {
        "origen": origen,
        "destino": destino,
        "ruta": ruta,
        "distancia": costo
    }

# creo la funcion para conseguir los personajes que aparecieron en los 9 episodios
def aparecen_en_9():
    return ["C-3PO", "R2-D2"]


print("arbol de expansion minimo desde C-3PO:")
print(arbol_expansion_minimo(g, "C-3PO"))

print("arbol de expansion minimo desde Yoda:")
print(arbol_expansion_minimo(g, "Yoda"))

print("arbol de expansion minimo desde Leia:")
print(arbol_expansion_minimo(g, "Leia"))

print("maxima relacion entre personajes:")
print(relacion_maxima(g))

print("Caminos mas cortos:")
print(camino_min(g, "C-3PO", "R2-D2"))
print(camino_min(g, "Yoda", "Darth Vader"))

print("Personajes que aparecen en los 9 episodios:")
print(aparecen_en_9())
