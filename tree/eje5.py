# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:

# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

from tree import BinaryTree

#Arbol donde guardo Nombre de los superheroes (True) y villanos (False)
arbol = BinaryTree()

characters = [
    ('Iron Man', True),
    ('Thanos', False),
    ('Captain America', True),
    ('Loki', False),
    ('Doctor Strangee', True),   # mal cargado
    ('Ultron', False),
    ('Hulk', True),
    ('Black Widow', True),
    ('Red Skull', False),
    ('Scarlet Witch', True),
    ('Green Goblin', False),
    ('Captain Marvel', True),
    ('Killmonger', False),
    ('Spider-Man', True),
    ('Vulture', False),
]

#b cargo los datos en el arbol (Inserto personajes) y listamos
for idx, (name, is_hero) in enumerate(characters, start=1):
    info = {'is_hero': is_hero, 'id': idx}
    arbol.insert(name, info)
    
print("arbol cargado alfabeticamente:")
arbol.in_order()

def listar_villanos(node):
    villanos = []
    if node is not None:
        villanos.extend(listar_villanos(node.left))
        if node.other_values["is_hero"] is False:
            villanos.append(node.value)
        villanos.extend(listar_villanos(node.right))
    return villanos

print("Villanos ordenados:")
print(listar_villanos(arbol.root))

# c. mostrar superhéroes que empiezan con 'C'
def heroes_con_C(node):
    heroes = []
    if node is not None:
        heroes.extend(heroes_con_C(node.left))
        if node.other_values["is_hero"] and node.value.startswith("C"):
            heroes.append(node.value)
        heroes.extend(heroes_con_C(node.right))
    return heroes

print("Heroes q empiezan con C:")
print(heroes_con_C(arbol.root))

#d Cuantos superhéroes hay en el árbol
def contar_heroes(node):
    if node is None:
        return 0
    count = contar_heroes(node.left) + contar_heroes(node.right)
    if node.other_values["is_hero"]:
        count += 1
    return count
print("Cantidad de heroes en el arbol:")
print(contar_heroes(arbol.root))

#e Corregir Doctor Strange
def corregir_nombre(tree, nombre_mal, nombre_bien):
    pos = tree.search(nombre_mal)
    if pos is not None:
        value, other_values = tree.delete(nombre_mal)
        tree.insert(nombre_bien, other_values)

corregir_nombre(arbol, "Doctor Strangee", "Doctor Strange")

print("arbol corregido")
arbol.in_order()


#f listar superheroes ordenados de manera descendente
def listar_heroes_desc(node):
    heroes = []
    if node is not None:
        heroes.extend(listar_heroes_desc(node.right))
        if node.other_values["is_hero"]:
            heroes.append(node.value)
        heroes.extend(listar_heroes_desc(node.left))
    return heroes
print("Heroes ordenados descendentemente:")
print(listar_heroes_desc(arbol.root))

#g generar un bosque a partir de este arbol, un árbol debe contener a los superheroes y otro a los villanos

heroes_tree = BinaryTree()
villanos_tree = BinaryTree()

def separar_arboles(node):
    if node is not None:
        separar_arboles(node.left)
        if node.other_values["is_hero"]:
            heroes_tree.insert(node.value, node.other_values)
        else:
            villanos_tree.insert(node.value, node.other_values)
        separar_arboles(node.right)
separar_arboles(arbol.root)

print("Arbol de heroes:")
heroes_tree.in_order()
print("Arbol de villanos:")
villanos_tree.in_order()

#I determinar cuantos nodos tiene cada arbol
def contar_nodos(node):
    if node is None:
        return 0
    return 1 + contar_nodos(node.left) + contar_nodos(node.right)
print("Cantidad de nodos en arbol de heroes:")
print(contar_nodos(heroes_tree.root))
print("Cantidad de nodos en arbol de villanos:")
print(contar_nodos(villanos_tree.root))
#II realizar un barrido ordenado alfabéticamente de cada árbol
print("Barrido ordenado alfabeticamente de arbol de heroes:")
heroes_tree.in_order()         
print("Barrido ordenado alfabeticamente de arbol de villanos:")
villanos_tree.in_order()
