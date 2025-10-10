# Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
# miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos
# tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
# siguientes consignas:
# a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
# b. realizar un barrido inorden del árbol por nombre y ranking;
# c. realizar un barrido por nivel de los árboles por ranking y especie;
# d. mostrar toda la información de Yoda y Luke Skywalker;
# e. mostrar todos los Jedi con ranking “Jedi Master”;
# f. listar todos los Jedi que utilizaron sabe de luz color verde;
# g. listar todos los Jedi cuyos maestros están en el archivo;
# h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
# i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

from tree import BinaryTree




jedis =  [
    ('Yoda', 'Unknown', -896, ['Green'], ['Jedi Master'], []),
    ('Luke Skywalker', 'Human', -19, ['Green', 'Blue'], ['Jedi Knight', 'Jedi Master'], ['Yoda', 'Obi-Wan Kenobi']),
    ('Anakin Skywalker', 'Human', -41, ['Blue'], ['Padawan', 'Jedi Knight'], ['Obi-Wan Kenobi']),
    ('Ahsoka Tano', 'Togruta', -36, ['Green', 'Blue'], ['Padawan'], ['Anakin Skywalker']),
    ('Mace Windu', 'Human', -72, ['Purple'], ['Jedi Master'], []),
    ('Plo Koon', 'Kel Dor', -382, ['Orange'], ['Jedi Master'], []),
    ('Ki-Adi-Mundi', 'Cerean', -92, ['Blue'], ['Jedi Master'], []),
]

#a
tree_name = BinaryTree()
tree_rank = BinaryTree()
tree_species = BinaryTree()

for idx, (name, species, birth, sabers, ranks, masters) in enumerate(jedis, start=1):
    data = {
        'species': species,
        'birth': birth,
        'sabers': sabers,
        'ranks': ranks,
        'masters': masters,
        'id': idx
    }
    tree_name.insert(name, data)
    for rank in ranks:
        tree_rank.insert(rank + '-' + name, data)
    tree_species.insert(species + '-' + name, data)

#b inorden de nombre y ranking

print("inorden de nombre")
tree_name.in_order()
print("inorden de rank")
tree_rank.in_order()

#c
print("level de rank")
tree_rank.by_level()
print("level de species")
tree_species.by_level()

#d
for jedi in ['Yoda', 'Luke Skywalker']:
    pos = tree_name.search(jedi)
    if pos:
        print(f"{pos.value} -> {pos.other_values}")

#e 
def listar_jedi_master(node):
  masters = []
  if node is not None:
    masters.extend(listar_jedi_master(node.left))
    if "Jedi Master" in node.other_values["ranks"]:
        masters.append(node.value)
    masters.extend(listar_jedi_master(node.right))
  return masters
print("Jedi Master:")
print(listar_jedi_master(tree_name.root))

#f
def listar_verdes(node):
    if node:
        listar_verdes(node.left)
        if 'Green' in node.other_values['sabers']:
            print(node.value)
        listar_verdes(node.right)

print("jedi con sable verde")
listar_verdes(tree_name.root)

#g
def maestros_en_archivo(node, tree):
    if node:
        maestros_en_archivo(node.left, tree)
        for maestro in node.other_values['masters']:
            if tree.search(maestro):
                print(node.value, "-> maestro:", maestro)
        maestros_en_archivo(node.right, tree)
print("Jedi cuyos maestros están en el archivo:")
maestros_en_archivo(tree_name.root, tree_name)

#h
def listar_especies(node):
    especies = []
    if node is not None:
      especies.extend(listar_especies(node.left))
      if node.other_values["species"] in ["Togruta", "Cerean"]:
          especies.append(node.value)
      especies.extend(listar_especies(node.right))
    return especies
print("Jedi de especie Togruta o Cerean:")
print(listar_especies(tree_name.root))

#i
def lista_A_y_guion(node):
  lista = []
  if node is not None:
    lista.extend(lista_A_y_guion(node.left))
    if node.value.startswith("A") or "-" in node.value:
        lista.append(node.value)
    lista.extend(lista_A_y_guion(node.right))
  return lista
print("Jedi que comienzan con A o tienen - en su nombre:")
print(lista_A_y_guion(tree_name.root))



          
    
