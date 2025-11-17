# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
from graph import Graph
import math

#cargamos la casa como grafo no dirigido
Casa = Graph(is_directed=False)
# ambientes de la casa creamos lista 
ambientes = [
    "Cocina", "Comedor", "Cochera", "Quincho",
    "Baño1", "Baño2", "Habitacion1", "Habitacion2",
    "SalaEstar", "Terraza", "Patio"
]
# Cargar todos los ambientes como vértices
for amb in ambientes:
    Casa.insert_vertex(amb)


# Conexiones entre ambientes (distancia en metros)
# Cocina y Comedor tendrán 5 conexiones cada uno 
# Todos los demás tendrán 3 conexiones como mínimo


conexiones = [
    # Cocina – 5 conexiones
    ("Cocina", "Comedor", 4),
    ("Cocina", "Baño1", 3),
    ("Cocina", "SalaEstar", 5),
    ("Cocina", "Patio", 7),
    ("Cocina", "Habitacion1", 6),

    # Comedor – 5 conexiones
    ("Comedor", "SalaEstar", 2),
    ("Comedor", "Terraza", 5),
    ("Comedor", "Patio", 4),
    ("Comedor", "Baño2", 6),
    ("Comedor", "Habitacion2", 8),

    # Cochera – 3 conexiones
    ("Cochera", "Quincho", 4),
    ("Cochera", "Patio", 9),
    ("Cochera", "Habitacion2", 7),

    # Quincho – 3 conexiones
    ("Quincho", "Patio", 5),
    ("Quincho", "Terraza", 6),
    ("Quincho", "Baño2", 8),

    # Baño1 – 3 conexiones
    ("Baño1", "Habitacion1", 2),
    ("Baño1", "SalaEstar", 3),
    ("Baño1", "Terraza", 7),

    # Baño2 – 3 conexiones
    ("Baño2", "Habitacion2", 3),
    ("Baño2", "Terraza", 4),
    ("Baño2", "Quincho", 8),

    # Habitacion1 – 3 conexiones
    ("Habitacion1", "SalaEstar", 4),
    ("Habitacion1", "Patio", 6),
    ("Habitacion1", "Baño1", 2),

    # Habitacion2 – 3 conexiones
    ("Habitacion2", "Terraza", 4),
    ("Habitacion2", "Cochera", 7),
    ("Habitacion2", "Baño2", 3),

    # SalaEstar – 3 conexiones
    ("SalaEstar", "Terraza", 3),
    ("SalaEstar", "Patio", 5),
    ("SalaEstar", "Comedor", 2),

    # Terraza – 3 conexiones
    ("Terraza", "Patio", 4),
    ("Terraza", "Quincho", 6),
    ("Terraza", "Comedor", 5),

    # Patio – 3 conexiones
    ("Patio", "Quincho", 5),
    ("Patio", "Cochera", 9),
    ("Patio", "Terraza", 4)
]

# Cargar todas las aristas en el grafo
for o, d, dist in conexiones:
    Casa.insert_edge(o, d, dist)

#funcion para reconstruir camino desde dijkstra
def reconstruir_camino(stack_path, destino):
    camino = []
    distancia = None

    while stack_path.size() > 0:
        nodo, dist, pred = stack_path.pop()

        if nodo == destino:
            if distancia is None:
                distancia = dist
            camino.append(nodo)
            destino = pred

    if not camino:
        return [], math.inf

    camino.reverse()
    return camino, distancia


#c obtenemos arbol de expansion minima y total de cable necesario
def arbolExpansion(grafo, vertice):
    tree_str = grafo.kruskal(vertice)

    total = 0   
    for edge in tree_str.split(";"): #aca usamos edge para separar las aristas 
        if "-" in edge:  # si contiene una arista
            o, d, w = edge.split("-") # separamos origen, destino y peso
            total += int(w)

    return f"Metros totales de cable necesarios: {total}"

#d camino mas corto desde habitacion1 hasta sala de estar
def habitacion1_a_sala(grafo):
    origen = "Habitacion1"
    destino = "SalaEstar"

    stack = grafo.dijkstra(origen)
    camino, distancia = reconstruir_camino(stack, destino)

    return {
        "origen": origen,
        "destino": destino,
        "camino": camino,
        "distancia": distancia
    }

print(arbolExpansion(Casa, "Cocina"))

respuesta = habitacion1_a_sala(Casa)
print("Camino más corto Habitacion1 s SalaEstar:")
print(respuesta)
