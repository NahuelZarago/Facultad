# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.


from tree import BinaryTree

criaturas_tree = BinaryTree()

#a
criaturas = [
    ('Ceto', '-'),
    ('Tifón', 'Zeus'),
    ('Equidna', 'Argos Panoptes'),
    ('Dino', '-'),
    ('Pefredo', '-'),
    ('Enio', '-'),
    ('Escila', '-'),
    ('Caribdis', '-'),
    ('Euríale', '-'),
    ('Esteno', '-'),
    ('Medusa', 'Perseo'),
    ('Ladón', 'Heracles'),
    ('Águila del Cáucaso', '-'),
    ('Quimera', 'Belerofonte'),
    ('Hidra de Lerna', 'Heracles'),
    ('León de Nemea', 'Heracles'),
    ('Esfinge', 'Edipo'),
    ('Dragón de la Cólquida', '-'),
    ('Cerbero', '-'),
    ('Cerda de Cromión', 'Teseo'),
    ('Toro de Creta', 'Teseo'),
    ('Jabalí de Calidón', 'Atalanta'),
    ('Carcinos', '-'),
    ('Gerión', 'Heracles'),
    ('Cloto', '-'),
    ('Láquesis', '-'),
    ('Átropo', '-'),
    ('Minotauro de Creta', 'Teseo'),
    ('Harpías', '-'),
    ('Argos Panoptes', 'Hermes'),
    ('Aves del Estínfalo', '-'),
    ('Talos', 'Medea'),
    ('Sirenas', '-'),
    ('Pitón', 'Apolo'),
    ('Cierva de Cerinea', '-'),
    ('Basilisco', '-'),
    ('Jabalí de Erimanto', '-')
]

for criatura, derrotado_por in criaturas:
    info = {
        'derrotado_por': derrotado_por,
        'descripcion': '',
        'capturada': ''
    }
    criaturas_tree.insert(criatura, info)

#c
pos = criaturas_tree.search('Talos')
if pos is not None:
    print(f"c) Informacion de {pos.value}: {pos.other_values}")
print()

#d
ranking = {}

def cargar_ranking(root):
    if root is not None:
        cargar_ranking(root.left)
        heroe = root.other_values['derrotado_por']
        if heroe != '-':
            ranking[heroe] = ranking.get(heroe, 0) + 1
        cargar_ranking(root.right)

cargar_ranking(criaturas_tree.root)

ranking_ordenado = sorted(ranking.items(), key=lambda x: x[1], reverse=True)
print("d) Top 3 heroes/dioses con mas criaturas derrotadas:")
print(ranking_ordenado[:3])
print()

#e
print("e) Criaturas derrotadas por Heracles:")
def derrotadas_por(root, nombre):
    if root is not None:
        derrotadas_por(root.left, nombre)
        if root.other_values['derrotado_por'].lower() == nombre.lower():
            print(root.value)
        derrotadas_por(root.right, nombre)

derrotadas_por(criaturas_tree.root, 'Heracles')
print()

#f
print("f) Criaturas no derrotadas:")
def no_derrotadas(root):
    if root is not None:
        no_derrotadas(root.left)
        if root.other_values['derrotado_por'] == '-':
            print(root.value)
        no_derrotadas(root.right)

no_derrotadas(criaturas_tree.root)
print()

#g h
capturadas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabali de Erimanto']
for nombre in capturadas:
    pos = criaturas_tree.search(nombre)
    if pos is not None:
        pos.other_values['capturada'] = 'Heracles'

#i
print("i) Coincidencias con 'dra':")
criaturas_tree.proximity_search('dra')
print()

#j
criaturas_tree.delete('Basilisco')
criaturas_tree.delete('Sirenas')

#k
pos = criaturas_tree.search('Aves del Estinfalo')
if pos is not None:
    pos.other_values['derrotado_por'] = 'Heracles (derroto a varias)'


#l
value, other_value = criaturas_tree.delete('Ladon')
if value is not None:
    criaturas_tree.insert('Dragon Ladon', other_value)

#m
print("m) Listado por nivel:")
criaturas_tree.by_level()
print()

#n
print("n) Criaturas capturadas por Heracles:")
def capturadas_por(root, heroe):
    if root is not None:
        capturadas_por(root.left, heroe)
        if root.other_values['capturada'].lower() == heroe.lower():
            print(root.value)
        capturadas_por(root.right, heroe)

capturadas_por(criaturas_tree.root, 'Heracles')
print()


#a
print("a) Listado inorden:")
criaturas_tree.in_order()
#