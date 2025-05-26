#Se tienen una cola con personajes de Marvel Cinematic Universe (MCU),
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe 
#y su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, 
# {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
#desarrollar un algoritmo que resuelva las siguientes actividades:
#a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
#b. mostrar los nombre de los superhéroes femeninos;
#c. mostrar los nombres de los personajes masculinos;
#d. determinar el nombre del superhéroe del personaje Scott Lang;
#e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#con la letra S;
#f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar 
# su nombre de superhéroes.

cola = [
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Stephen Strange", "Doctor Strange", "M"),
    ("Shuri", "Black Panther", "F")
]

#a
def determinar_Capitana_Marvel(cola):
  for especificaciones in cola:
    if especificaciones[1] == "Capitana Marvel":
        return especificaciones[0]
  return "No se encontro la capitana marvel"
      
#b
def Nombres_Femeninos(cola):
  lista = []
  for especificaciones in cola:
    if especificaciones[2] == "F":
        lista.append(especificaciones)
  return lista

#c
def Nombres_Masculinos(cola):
  lista = []
  for especificaciones in cola:
    if especificaciones[2] == "M":
      lista.append(especificaciones)
  return lista
      
#d
def Determinar_Scott_Lang(cola):
  for especificaciones in cola:
    if especificaciones[0] == "Scott Lang":
      return especificaciones[1]
  return "No se encontro a Scott Lang"
      
#e
def Nombres_S(cola):
  lista = []  
  for especificaciones in cola:
    if especificaciones[0].startswith("S") or especificaciones[1].startswith("S"):
      lista.append(especificaciones)
  return lista 

#f
def Encontrar_Carol_Danvers(cola):
  encontrado = False
  for especificaciones in cola:
    if especificaciones[0] == "Carol Danvers":
      print("Carol Danvers esta en la cola y su superheroe es: ", especificaciones[1])
      encontrado = True
      break
  if not encontrado:
    print("Carol davers no esta en la lista")
    
#---------------------------------------------------------------------------------------    
    
print("El personaje de Capitana Marvel es:", determinar_Capitana_Marvel(cola))
print()

print("Los nombres de los superheroes femeninos son:")
for especificaciones in Nombres_Femeninos(cola):
    print(especificaciones[1])
print()

print("Los nombres de los personajes masculinos son:")
for especificaciones in Nombres_Masculinos(cola):
    print(especificaciones[0])
print()

print("El superheroe del personaje Scott Lang es:", Determinar_Scott_Lang(cola))
print()

print("Personajes o superheroes que empiezan con S:")
for especificaciones in Nombres_S(cola):
  print(especificaciones[0], especificaciones[1], especificaciones[2])
print()

Encontrar_Carol_Danvers(cola)

