# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
# sarios para resolver las tareas, listadas a continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
# dor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;

from graph import Graph




grafo = Graph(is_directed=False)

#  Datos de personajes + episodios donde aparecen 
personajes_info = {
    "Luke Skywalker": [1,2,3,4,5,6,7,8,9],
    "Darth Vader": [1,2,3,4,5,6],
    "Yoda": [1,2,3,4,5,6,8],
    "Boba Fett": [2,5,6],
    "C-3PO": [1,2,3,4,5,6,7,8,9],
    "Leia": [1,2,3,4,5,6,7,8,9],
    "Rey": [7,8,9],
    "Kylo Ren": [7,8,9],
    "Chewbacca": [1,2,3,4,5,6,7,8,9],
    "Han Solo": [1,2,3,4,5,6,7],
    "R2-D2": [1,2,3,4,5,6,7,8,9],
    "BB-8": [7,8,9]
}

# Insertar vertices
for nombre in personajes_info.keys():
    grafo.insert_vertex(nombre)

# Aristas: cantidad de episodios compartidos 
conexiones = [
    ("Luke Skywalker", "Darth Vader", 4),
    ("Luke Skywalker", "Yoda", 3),
    ("Luke Skywalker", "Leia", 6),
    ("Luke Skywalker", "Han Solo", 5),
    ("Luke Skywalker", "R2-D2", 7),

    ("Darth Vader", "Leia", 4),
    ("Darth Vader", "Kylo Ren", 2),

    ("Yoda", "C-3PO", 2),
    ("Yoda", "Rey", 1),

    ("C-3PO", "R2-D2", 9),
    ("C-3PO", "Leia", 7),
    ("C-3PO", "Han Solo", 4),

    ("Han Solo", "Chewbacca", 9),
    ("Han Solo", "Leia", 6),
    ("Han Solo", "Kylo Ren", 1),

    ("Rey", "BB-8", 3),
    ("Rey", "Kylo Ren", 3),

    ("BB-8", "R2-D2", 1)
]

# Cargar aristas
for o, d, w in conexiones:
    grafo.insert_edge(o, d, w)


#genero el arbol de expansion minima con Prim
def prim_mst(grafo, inicio):
    visitados = set([inicio])
    aristas_candidatas = []

    origen = grafo.search(inicio)
    for edge in origen.edges:
        aristas_candidatas.append((inicio, edge.value, edge.other_value))

    resultado = []

    while len(visitados) < grafo.size():
        aristas_candidatas.sort(key=lambda x: x[2])
        mejor = None

        for a in aristas_candidatas:
            if a[1] not in visitados:
                mejor = a
                break

        if mejor is None:
            break

        resultado.append(mejor)
        nuevo = mejor[1]
        visitados.add(nuevo)

        nodo_nuevo = grafo.search(nuevo)
        for edge in nodo_nuevo.edges:
            if edge.value not in visitados:
                aristas_candidatas.append((nuevo, edge.value, edge.other_value))

    return resultado

def mostrar_mst(personaje):
    print(f"MST desde {personaje}")
    mst = prim_mst(grafo, personaje)
    for o, d, peso in mst:
        print(f"{o} ---{peso}→ {d}")


#maximo número de episodios compartidos
def max_relacion(grafo):
    maximo = 0
    pares = []

    for v in grafo:
        for edge in v.edges:
            if edge.weight > maximo:
                maximo = edge.weight
                pares = [(v.value, edge.value)]
            elif edge.weight == maximo:
                pares.append((v.value, edge.value))
    return maximo, pares


#Caminos más cortos (Dijkstra del profe)
def mostrar_camino(origen, destino):
    stack = grafo.dijkstra(origen)

    recorrido = []
    costo = None

    while stack.size() > 0:
        nodo, dist, padre = stack.pop()
        if nodo == destino:
            if costo is None:
                costo = dist
            recorrido.append(nodo)
            destino = padre

    recorrido.reverse()

    print(f"Camino más corto {origen} → {recorrido[-1]}:")
    print(" -> ".join(recorrido), f"(costo: {costo})")


#Personajes que aparecieron en los 9 episodios
def personajes_nueve_eps(info):
    return [p for p, eps in info.items() if len(eps) == 9]



mostrar_mst("C-3PO")
mostrar_mst("Yoda")
mostrar_mst("Leia")


print("Maximo número de episodios compartidos ")
maxi, pares = max_relacion(grafo)
print("Valor máximo:", maxi)
print("Pares:")
for p in set(pares):
    print("  ", p)


mostrar_camino("C-3PO", "R2-D2")
mostrar_camino("Yoda", "Darth Vader")


print("Personajes que aparecen en los 9 episodios")
for p in personajes_nueve_eps(personajes_info):
    print("  ", p)
