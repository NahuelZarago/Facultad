# Desarrollar un algoritmo que permita cargar el índice del libro Ingeniería de Software de Ian
# Summerville de manera automática desde un archivo de texto, transformando el árbol n-ario
# del índice en un árbol binario no balanceado mediante el uso de la transformada de Knuth,
# para resolver las siguientes actividades:
# a. listar el índice en su orden original;
# b. mostrar la parte del índice correspondiente al subtitulo “Diseño de software
# de tiempo real”;
# c. deberá almacenar además del texto de índice la página del libro donde está dicho tema;
# d. determinar cuántos capítulos tiene;
# e. determinar todos los temas que contengan las palabras modelo y métrica.

from tree import BinaryTree


index_tree = BinaryTree()


index = [
    ("Capítulo 1: Introduccion", 3),
    ("Capítulo 2: Procesos de software", 35),
    ("Capítulo 3: Ingenieria de requerimientos", 73),
    ("Capítulo 4: Diseño de software", 115),
    ("Diseño de tiempo real", 150),
    ("Capítulo 5: Verificacion y validacion", 200),
    ("Capítulo 6: Gestión de proyectos de software", 250),
    ("Capítulo 7: Métricas y modelos", 300),
]


for item in index:
    tema, pagina = item
    info = {
        'page': pagina
    }
    index_tree.insert(tema, info)

#a
print("indice en orden (in-order):")
index_tree.in_order()
print()

#b
print("Subtitulo buscado:")
pos = index_tree.search("Diseño de tiempo real")
if pos is not None:
    print(f"{pos.value}, pagina {pos.other_values['page']}")
print()

#d
def count_chapters(root):
    if root is None:
        return 0
    count = 0
    if str(root.value).startswith("Capitulo"):
        count += 1
    count += count_chapters(root.left)
    count += count_chapters(root.right)
    return count

print("Cantidad de capitulos:", count_chapters(index_tree.root))
print()

#e
def search_keywords(root, keywords):
    if root is not None:
        search_keywords(root.left, keywords)
        text = root.value.lower()
        if any(k in text for k in keywords):
            print(f"{root.value}, pagina {root.other_values['page']}")
        search_keywords(root.right, keywords)

print("Temas con 'modelo' o 'metrica':")
search_keywords(index_tree.root, ["modelo", "metrica"])
