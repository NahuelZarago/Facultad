#Dada una cola con las notificaciones de las aplicaciones de redes sociales de 
#un Smartphone,
#de las cual se cuenta con la hora de la notificación, la aplicación que la emitió 
# y el mensaje,
#resolver las siguientes actividades:
#a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
#b. escribir una función que muestre todas las notificaciones de Twitter, 
# cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
#c. utilizar una pila para almacenar temporáneamente las notificaciones 
# producidas entre las 11:43 y las 15:57, y determinar cuántas son.

cola = [
    ("09:00", "Facebook", "Mensaje de mi amigo"),
    ("9:30", "Instagram", "Nueva post de mi amigo"),
    ("10:00", "WhatsApp", "Mensaje de mi amigo para estudiar"),
    ("11:00", "Facebook", "Historia que subio mi amigo"),
    ("11:48", "Twitter", "Cursito de Python creado por mi amigo"),
    ("13:00", "Facebook", "Mensajito de mi amigo"),
    ("15:30", "Instagram" "Nueva publicacion de mi amigo"),
    #Hacia de todo mi amigo jaja
]

#a
def eliminarFacebook(cola):
  nueva_cola = []
  for noti_cola in cola:
    if noti_cola[1] != "Facebook":
      nueva_cola.append(noti_cola)
  return nueva_cola

#B
def noti_twitter(cola):
  for noti_cola in cola:
    if noti_cola[1] == "Twitter" and "Python" in noti_cola[2]:
      print(noti_cola)

#C
def pila(cola):
  pilaVacia = []
  for noti_cola in cola:
    if "11:43" < noti_cola[0] < "15:57":
      pilaVacia.append(noti_cola)
  print(len(pilaVacia))     
  
  
print("Cola sin facebook:")
print(eliminarFacebook)

print("notificaciones de twiter con python:")
noti_twitter(cola)
print()
pila(cola)
