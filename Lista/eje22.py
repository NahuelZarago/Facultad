# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su 
# nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias 
# para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from list_ import List

def order_by_name(item):
    return item.name

def order_by_species(item):
    return item.species


class Jedi:
    def __init__(self, name, masters, sables, species):
        self.name = name
        self.masters = masters        
        self.sables = sables
        self.species = species

    def __str__(self):
        return (f"Nombre: {self.name} | "
                f"Maestros: {', '.join(self.masters) if self.masters else 'Ninguno'} | "
                f"Colores sable: {', '.join(self.sables)} | "
                f"Especie: {self.species}")



jedis_data = [
    {"name": "Ahsoka Tano", "masters": ["Anakin Skywalker"], "lightsaber_colors": ["green", "blue", "white"], "species": "Togruta"},
    {"name": "Kit Fisto", "masters": ["Yoda"], "lightsaber_colors": ["green"], "species": "Nautolano"},
    {"name": "Luke Skywalker", "masters": ["Obi-Wan Kenobi", "Yoda"], "lightsaber_colors": ["green", "blue"], "species": "Human"},
    {"name": "Anakin Skywalker", "masters": ["Obi-Wan Kenobi"], "lightsaber_colors": ["blue"], "species": "Human"},
    {"name": "Obi-Wan Kenobi", "masters": ["Qui-Gon Jin"], "lightsaber_colors": ["blue"], "species": "Human"},
    {"name": "Yoda", "masters": [], "lightsaber_colors": ["green"], "species": "Unknown"},
    {"name": "Qui-Gon Jin", "masters": ["Count Dooku"], "lightsaber_colors": ["green"], "species": "Human"},
    {"name": "Mace Windu", "masters": [], "lightsaber_colors": ["violet"], "species": "Human"},
    {"name": "Aayla Secura", "masters": ["Quinlan Vos"], "lightsaber_colors": ["blue"], "species": "Twi'lek"},
]


#criterios
list_jedi = List()
list_jedi.add_criterion('name', order_by_name)
list_jedi.add_criterion('species', order_by_species)

for jedi_data in jedis_data:
    jedi = Jedi(
        name=jedi_data["name"],
        masters=jedi_data["masters"],
        sables=jedi_data["sables"],
        species=jedi_data["species"]
    )
    list_jedi.append(jedi)


#a
print("A) Listado por nombre:")
list_jedi.sort_by_criterion('name')
list_jedi.show()

print("A) Listado por especie:")
list_jedi.sort_by_criterion('species')
list_jedi.show()


#b
print("B) Info de Ahsoka Tano y Kit Fisto:")
for name in ["Ahsoka Tano", "Kit Fisto"]:
    pos = list_jedi.search(name, 'name')
    if pos is not None:
        print(list_jedi[pos])


#c
print("C) Padawans de Yoda y Luke Skywalker:")
for master in ["Yoda", "Luke Skywalker"]:
    print(f"Aprendices de {master}:")
    for jedi in list_jedi:
        if master in jedi.masters:
            print("  ", jedi.name)


#d
print("D) Jedi Humanos y Twi'lek:")
for jedi in list_jedi:
    if jedi.species in ["Human", "Twi'lek"]:
        print(jedi)


#e
print("E) Jedi que comienzan con A:")
for jedi in list_jedi:
    if jedi.name.startswith("A"):
        print(jedi)


#f
print("F) Jedi con mas de un color de sable:")
for jedi in list_jedi:
    if len(jedi.sables) > 1:
        print(jedi)


#g
print("G) Jedi con sable amarillo o violeta:")
for jedi in list_jedi:
    if "yellow" in jedi.sables or "violet" in jedi.sables:
        print(jedi)


#h
print("H) Padawans de Qui-Gon Jin y Mace Windu:")
for master in ["Qui-Gon Jin", "Mace Windu"]:
    print(f"Padawans de {master}:")
    found = False
    for jedi in list_jedi:
        if master in jedi.masters:
            print("  ", jedi.name)
            found = True
    if not found:
        print("Ninguno")
 