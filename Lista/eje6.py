#Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
#casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
#rias para poder realizar las siguientes actividades:
#a. eliminar el nodo que contiene la información de Linterna Verde;
#b. mostrar el año de aparición de Wolverine;
#c. cambiar la casa de Dr. Strange a Marvel;
#d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
#f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
#g. mostrar toda la información de Flash y Star-Lord;
#h. listar los superhéroes que comienzan con la letra B, M y S;
#i. determinar cuántos superhéroes hay de cada casa de comic.
from list_ import List 


class Superheroe:
    def __init__(self, nombre, año, casa, biografia):
        self.nombre = nombre
        self.año = año
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return f"{self.nombre} ({self.año}) - {self.casa}: {self.biografia}"

# Funciones criterio (se utiliza para buscar)
def criterio_nombre(s): return s.nombre
def criterio_año(s): return s.año


heroes = List([
    Superheroe("Wolverine", 1974, "Marvel", "Tiene un esqueleto de adamantium."),
    Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo con gran poder."),
    Superheroe("Dr. Strange", 1963, "DC", "Hechicero supremo con capa mágica."),
    Superheroe("Iron Man", 1963, "Marvel", "Construyó una armadura para sobrevivir."),
    Superheroe("Batman", 1939, "DC", "Vigilante con traje negro."),
    Superheroe("Capitana Marvel", 1968, "Marvel", "Piloto militar con superpoderes."),
    Superheroe("Mujer Maravilla", 1941, "DC", "Princesa amazona con traje de combate."),
    Superheroe("Flash", 1940, "DC", "El hombre más rápido del mundo."),
    Superheroe("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia."),
    Superheroe("Spider-Man", 1962, "Marvel", "Joven con poderes arácnidos."),
    Superheroe("Superman", 1938, "DC", "Usa traje con capa y símbolo 'S'."),
])


heroes.add_criterion("nombre", criterio_nombre)
heroes.add_criterion("año", criterio_año)

#a
heroes.delete_value("Linterna Verde", "nombre")

#b
index = heroes.search("Wolverine", "nombre")
print("b.", heroes[index].año if index is not None else "No encontrado")

#c
index = heroes.search("Dr. Strange", "nombre")
if index is not None:
    heroes[index].casa = "Marvel"

#d
print("d.")
for h in heroes:
    bio = h.biografia.lower()
    if "traje" in bio or "armadura" in bio:
        print(h.nombre)

#e
print("e.")
for h in heroes:
    if h.año < 1963:
        print(f"{h.nombre} - {h.casa}")

#f
print("f.")
for name in ["Capitana Marvel", "Mujer Maravilla"]:
    index = heroes.search(name, "nombre")
    if index is not None:
        print(f"{name}: {heroes[index].casa}")
    else:
        print(f"{name}: No encontrada")

#g
print("g.")
for name in ["Flash", "Star-Lord"]:
    index = heroes.search(name, "nombre")
    if index is not None:
        print(heroes[index])

#h
print("h.")
for h in heroes:
    if h.nombre[0] in ("B", "M", "S"):
        print(h.nombre)

#i
print("i.")
contadores = {}
for h in heroes:
    contadores[h.casa] = contadores.get(h.casa, 0) + 1
for casa, cantidad in contadores.items():
    print(f"{casa}: {cantidad}")

      
