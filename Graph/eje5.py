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

red = Graph(is_directed=False)

# Insertar equipos con nombre que incluye tipo
red.insert_vertex("Red Hat", {"tipo": "notebook"})
red.insert_vertex("Debian", {"tipo": "notebook"})
red.insert_vertex("Arch", {"tipo": "notebook"})
red.insert_vertex("Manjaro", {"tipo": "pc"})
red.insert_vertex("Fedora", {"tipo": "pc"})
red.insert_vertex("Impresora", {"tipo": "impresora"})
red.insert_vertex("Guarani", {"tipo": "servidor"})
red.insert_vertex("Switch1", {"tipo": "switch"})
red.insert_vertex("Switch2", {"tipo": "switch"})
red.insert_vertex("MongoDB", {"tipo": "servidor"})
red.insert_vertex("Ubuntu", {"tipo": "pc"})
red.insert_vertex("Mint", {"tipo": "pc"})
red.insert_vertex("Router1", {"tipo": "router"})
red.insert_vertex("Router2", {"tipo": "router"})
red.insert_vertex("Router3", {"tipo": "router"})
red.insert_vertex("Parrot", {"tipo": "pc"})

conexiones = [
    ("Ubuntu", "Switch1", 18),
    ("Impresora", "Switch1", 22),
    ("Mint", "Switch1", 80),
    ("Debian", "Switch1", 17),
    ("Switch1", "Router1", 29),
    ("Router1", "Router2", 37),
    ("Router1", "Router3", 43),
    ("Router2", "Router3", 50),
    ("Router2", "Guarani", 9),
    ("Router2", "Red Hat", 25),
    ("Router3", "Switch2", 61),
    ("Switch2", "Fedora", 3),
    ("Switch2", "Arch", 56),
    ("Switch2", "Manjaro", 40),
    ("Switch2", "Parrot", 12),
    ("Switch2", "MongoDB", 5)
    ]


for origen, destino, peso in conexiones:
    red.insert_edge(origen, destino, peso)


def barridos_originales(grafo):
    notebooks = ["Red Hat", "Debian", "Arch"]
    
    for notebook in notebooks:
        grafo.deep_sweep(notebook)
        grafo.amplitude_sweep(notebook)
        
    return print("Barridos completados")



def obtener_caminos_impresora(grafo):

    pcs = ["Manjaro", "Red Hat", "Fedora"]    
    resultados = {}   
    
    for pc in pcs:
        path = grafo.dijkstra(pc) #todos los caminos mas cortos a pc
        destination = 'Impresora'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0: #mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destination: #chequea hasta que sea la impresora
                if peso_total is None:
                    peso_total = value[1] #añade el peso
                camino_completo.append(value[0]) #añade la impresora al camino
                destination = value[2] #añade el predecesor de la impresora y vuelve a hacer esto
        
        camino_completo.reverse() #Lo inverte para que sea de pc a impresora

        resultados[pc] = { #Aca construye el camino
            "camino": camino_completo,
            "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
        }
    
    return resultados


def arbolExpansion(arbol, vertice):
    tree = arbol.kruskal(vertice)
    peso_total = 0

    for edge in tree.split(';'):
        origin, destination, weight = edge.split('-')
        print(f"Arista: {origin} - {destination}, Peso: {weight}")
        peso_total += int(weight)

    return peso_total


def obtener_caminos_Guarani(grafo):
    pcs = ["Manjaro", "Parrot", "Fedora", "Ubuntu", "Mint"]    
    resultados = {}   
    
    for pc in pcs:
        path = grafo.dijkstra(pc)  # Todos los caminos más cortos desde pc
        destination = 'Guarani'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0:  # Mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destination:  # Chequea hasta que sea Guarani
                if peso_total is None:
                    peso_total = value[1]  # Añade el peso
                camino_completo.append(value[0])  # Añade Guarani al camino
                destination = value[2]  # Añade el predecesor de Guarani y vuelve a hacer esto
        
        camino_completo.reverse()  # Lo invierte para que sea de pc a Guarani

        resultados[pc] = {  # Aca construye el camino
            "camino": camino_completo,
            "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
        }
    
    return resultados


def obtener_caminos_MongoDB(grafo):
    pcs = ["Ubuntu", "Mint"]    
    resultados = {}   
    
    for pc in pcs:
        path = grafo.dijkstra(pc)  # Todos los caminos más cortos desde pc
        destination = 'MongoDB'
        peso_total = None
        camino_completo = []
        
        while path.size() > 0:  # Mientras que el path tenga algo, hace un pop al value
            value = path.pop()
            if value[0] == destination:  # Chequea hasta que sea MongoDB
                if peso_total is None:
                    peso_total = value[1]  # Añade el peso
                camino_completo.append(value[0])  # Añade MongoDB al camino
                destination = value[2]  # Añade el predecesor de MongoDB y vuelve a hacer esto
        
        camino_completo.reverse()  # Lo invierte para que sea de pc a MongoDB

        resultados[pc] = {  # Aca construye el camino
            "camino": camino_completo,
            "distancia": peso_total if peso_total is not None and peso_total != math.inf else math.inf
        }
    
    return resultados


def cambiar_ImpresoraYResolverB(red):
    red.delete_edge("Impresora", "Switch1")
    red.insert_edge("Impresora", "Router2", 22)

    notebooks = ["Red Hat", "Debian", "Arch"]
    
    for notebook in notebooks:
        red.deep_sweep(notebook)
        red.amplitude_sweep(notebook)


print(barridos_originales(red))
print(obtener_caminos_impresora(red))
print(arbolExpansion(red, "Impresora"))
print(obtener_caminos_Guarani(red))
print(obtener_caminos_MongoDB(red))
print(cambiar_ImpresoraYResolverB(red))
