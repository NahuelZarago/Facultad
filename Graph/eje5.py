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
import math

#a cargamos la red con todos los tipos de nodos
# Creamos grafo NO dirigido
red = Graph(is_directed=False)

# Diccionario de nodos con su tipo 
equipos = {
    "LaptopA": "notebook",
    "LaptopB": "notebook",
    "LaptopC": "notebook",

    "WorkPC": "pc",
    "OfficePC": "pc",
    "GamerPC": "pc",

    "PrinterX": "impresora",

    "Srvguarani": "servidor",
    "SrvDatos": "servidor",

    "Switch01": "switch",
    "Switch02": "switch",

    "RtAlpha": "router",
    "RtBeta": "router",
    "RtGamma": "router",
}

# Insertamos cada vértice con su tipo dentro de "other_values"
for nombre, tipo in equipos.items():
    red.insert_vertex(nombre, {"tipo": tipo})



# Lista con las aristas: origen, destino, peso
conexiones = [
    ("LaptopA", "Switch01", 10),
    ("LaptopB", "Switch01", 15),
    ("OfficePC", "Switch01", 22),

    ("Switch01", "RtAlpha", 12),

    ("RtAlpha", "RtBeta", 18),
    ("RtBeta", "Srvguarani", 9),
    ("RtAlpha", "LaptopC", 25),

    ("RtBeta", "RtGamma", 14),
    ("RtGamma", "Switch02", 30),

    ("Switch02", "WorkPC", 3),
    ("Switch02", "GamerPC", 11),
    ("Switch02", "PrinterX", 20),
    ("Switch02", "SrvDatos", 5),
]

# Cargamos las aristas en el grafo de conexiones
for o, d, w in conexiones:
    red.insert_edge(o, d, w)

#funcion para reconstruir camino desde dijkstra 
def reconstruir_camino(stack_path, destino):
    # Esta función toma la pila que retorna dijkstra() y arma el camino final

    camino = []
    distancia = None

    # Recorremos la pila hasta vaciarla
    while stack_path.size() > 0:
        nodo, dist, pred = stack_path.pop()

        # Si encontramos el destino buscado
        if nodo == destino:
            # Guardamos la distancia final solo la primera vez
            if distancia is None:
                distancia = dist

            # Agregamos el nodo actual al camino
            camino.append(nodo)

            # Saltamos al predecesor para seguir reconstruyendo
            destino = pred

    # Si no se encontró ruta, devolvemos vacío
    if not camino:
        return [], math.inf

    # Invertimos la lista para que quede en orden origen hacia destino
    camino.reverse()
    return camino, distancia



#barrido solo por amplitud desde las notebooks 
def barridos_notebooks(grafo):
    # Se realizará busqueda en amplitud desde cada notebook
    notebooks = ["LaptopA", "LaptopB", "LaptopC"]

    print("barrido de la red desde notebooks:\n")

    for nb in notebooks:
        print(f"{nb}:")
        grafo.amplitude_sweep(nb)   # Barrido en amplitud
        print("")



#c camino mas corto a impresora desde varias pcs
def caminos_a_impresora(grafo):
    # PCs/notebooks desde donde se quiere enviar a imprimir un archivo
    pcs = ["WorkPC", "LaptopA", "GamerPC"]

    destino = "PrinterX"
    resultados = {}

    for pc in pcs:
        # Ejecutamos dijkstra desde cada PC
        stack = grafo.dijkstra(pc)

        # Reconstruimos el camino final hacia la impresora
        camino, dist = reconstruir_camino(stack, destino)

        # Guardamos los resultados
        resultados[pc] = {"camino": camino, "distancia": dist}

    return resultados

#d arbol de expansion minima con kruskal 
def mst_kruskal(grafo):
    # Kruskal devuelve un string de aristas tipo: "A-B-10;C-D-5;..."
    texto = grafo.kruskal("LaptopA")
    total = 0

    # Sumamos pesos del árbol
    if isinstance(texto, str):
        partes = texto.split(";")
        for edge in partes:
            if "-" in edge:
                o, d, w = edge.split("-")
                total += int(w)

    return total, texto


#e pc mas cercana a srvguarani
def pc_mas_cercana_a_academico(grafo):
    # Solo computadoras reales (no notebooks)
    pcs = ["WorkPC", "OfficePC", "GamerPC"]

    destino = "Srvguarani"

    mejor_pc = None
    mejor_dist = math.inf
    mejor_camino = []

    # Probamos cada PC
    for pc in pcs:
        stack = grafo.dijkstra(pc)
        camino, dist = reconstruir_camino(stack, destino)

        # Elegimos la distancia más corta
        if dist < mejor_dist:
            mejor_dist = dist
            mejor_pc = pc
            mejor_camino = camino

    return {"pc": mejor_pc, "distancia": mejor_dist, "camino": mejor_camino}


#f pc del switch mas cercana a srvdatos

def pc_del_switch_mas_cercana_a_datos(grafo):
    # Buscamos la posición del switch en el grafo
    pos = grafo.search("Switch01", "value")
    vecinos = grafo[pos].edges   # Aristas que salen del switch

    candidatos = []

    # Filtramos solo vecinos que sean PCs
    for edge in vecinos:
        nombre = edge.value
        pos2 = grafo.search(nombre, "value")
        data = grafo[pos2].other_values
        tipo = data.get("tipo")

        if tipo == "pc":
            candidatos.append(nombre)

    destino = "SrvDatos"

    mejor_pc = None
    mejor_dist = math.inf
    mejor_camino = []

    # Ejecutamos Dijkstra desde cada PC conectada
    for pc in candidatos:
        stack = grafo.dijkstra(pc)
        camino, dist = reconstruir_camino(stack, destino)

        # Elegimos la menor distancia
        if dist < mejor_dist:
            mejor_dist = dist
            mejor_pc = pc
            mejor_camino = camino

    return {
        "pc": mejor_pc,
        "distancia": mejor_dist,
        "camino": mejor_camino,
        "candidatos": candidatos
    }


if __name__ == "__main__":

    # Mostrar vértices cargados con su tipo
    print("Tipos de dispositivos cargados ")
    for v in red:
        print(v.value, " tipo:", v.other_values["tipo"])

    # Realizar BFS desde notebooks
    barridos_notebooks(red)

    # Mostrar caminos a impresora
    print("Camino más corto a la impresora")
    resultados = caminos_a_impresora(red)
    for pc, info in resultados.items():
        print(f"{pc}: camino = {info['camino']} | distancia = {info['distancia']}")

    # Obtener y mostrar árbol de expansión mínima
    print("Árbol de Expansión Mínima")
    peso, texto = mst_kruskal(red)
    print("Aristas:", texto)
    print("Peso total:", peso)

    # PC más cercana a Srvguarani
    print("PC más cercana a Srvguaranidemico")
    r = pc_mas_cercana_a_academico(red)
    print(r)

    # PC del Switch01 más cercana a SrvDatos
    print("PC del Switch01 más cercana a SrvDatos ")
    r = pc_del_switch_mas_cercana_a_datos(red)
    print(r)
