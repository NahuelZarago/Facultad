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


import queue_  
import stack


class Notificacion:
    def __init__(self, hora: str, app: str, mensaje: str):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

    def __str__(self):
        return f"{self.hora} - {self.app} - {self.mensaje}"

notificaciones = [
    Notificacion("09:00", "Facebook", "Mensaje de mi amigo"),
    Notificacion("09:30", "Instagram", "Nueva post de mi amigo"),
    Notificacion("10:00", "WhatsApp", "Mensaje de mi amigo para estudiar"),
    Notificacion("11:00", "Facebook", "Historia que subió mi amigo"),
    Notificacion("11:48", "Twitter", "Cursito de Python creado por mi amigo"),
    Notificacion("13:00", "Facebook", "Mensajito de mi amigo"),
    Notificacion("15:30", "Instagram", "Nueva publicación de mi amigo"),
]

cola_notis = queue.Queue()
for noti in notificaciones:
    cola_notis.arrive(noti)

#a
def eliminar_facebook(cola: queue.Queue):
    for i in range(cola.size()):
        if cola.on_front().app != "Facebook":
            cola.move_to_end()
        else:
            cola.attention()
#b
def mostrar_twitter_python(cola: queue.Queue):
    for i in range(cola.size()):
        noti = cola.on_front()
        if noti.app == "Twitter" and "Python" in noti.mensaje:
            print(noti)
        cola.move_to_end()
#c
def notis_en_horario(cola: queue.Queue):
    pila_horario = stack.Stack()
    for i in range(cola.size()):
        noti = cola.on_front()
        if "11:43" < noti.hora < "15:57":
            pila_horario.push(noti)
        cola.move_to_end()

    print(f"Cantidad de notificaciones entre 11:43 y 15:57: {pila_horario.size()}")


print("Notificaciones eliminadas")
eliminar_facebook(cola_notis)
notificaciones()
print("Notificaciones de Twitter con 'Python' en el mensaje:")
mostrar_twitter_python(cola_notis)
print("Contando notificaciones entre 11:43 y 15:57:")
notis_en_horario(cola_notis)

