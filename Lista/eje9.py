#9. Se tiene una lista de los alumnos de un curso, de los que se sabe nombre, apellido y legajo.
#Por otro lado se tienen las notas de los diferentes parciales que rindió cada uno de ellos con
#la siguiente información: materia que rindió, nota obtenida y fecha de parcial. Desarrollar un
#algoritmo que permita realizar la siguientes actividades:
#a. mostrar los alumnos ordenados alfabéticamente por apellido;
#b. indicar los alumnos que no desaprobaron ningún parcial;
#c. determinar los alumnos que tienen promedio mayor a 8,89;
#d. mostrar toda la información de los alumnos cuyos apellidos comienzan con L;
#e. mostrar el promedio de cada uno de los alumnos;
#f. mostrar todos los alumnos que rindieron la cátedra “Algoritmos y estructuras de datos”;
#g. indicar el porcentaje de parciales aprobados de un alumno indicado por el usuario;
#h. indicar cuantos alumnos aprobaron y desaprobaron parciales de la cátedra “Base de datos”;
#i. mostrar todos los alumnos que rindieron en el año 2020;
#j. debe modificar el TDA para implementar lista de lista.

from list_ import List 


class Alumno:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.parciales = []
        
    def agregar_parcial(self, parcial):
        self.parciales.append(parcial)

    def __str__(self):
        return f"{self.nombre} ({self.apellido}) - {self.legajo}"

class Parcial:
    def __init__(self, materia, nota, fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return f"{self.materia} ({self.nota}) - {self.fecha}"


alumnos = [
    Alumno("Juana", "Gonzalez", 45),
    Alumno("Mariano", "Perez", 32),
    Alumno("Mariano", "Perez", 51),
    Alumno("Carlos", "Romero", 14),
    Alumno("Ana", "Cordoba", 29),
]

alumnos[0].agregar_parcial(Parcial("Algoritmos y estructuras de datos", 9, "2020-03-10"))
alumnos[0].agregar_parcial(Parcial("Base de datos", 8, "2020-05-15"))
alumnos[1].agregar_parcial(Parcial("Algoritmos y estructuras de datos", 6, "2020-04-12"))
alumnos[1].agregar_parcial(Parcial("Base de datos", 5, "2020-06-10"))
alumnos[2].agregar_parcial(Parcial("Algoritmos y estructuras de datos", 10, "2020-02-20"))
alumnos[2].agregar_parcial(Parcial("Base de datos", 9, "2020-05-05"))
alumnos[3].agregar_parcial(Parcial("Algoritmos y estructuras de datos", 5, "2020-07-01"))
alumnos[4].agregar_parcial(Parcial("Base de datos", 8, "2020-08-20"))

#a
def mostrar_alumnos_ordenados_por_apellido(alumnos):
  lista = List()
  for a in alumnos:
        lista.append(a)
  lista.sort_by_criterion("apellido")
  print("Alumnos ordenados por apellido:")
  lista.show()

def criterio_apellido(alumno):
    return alumno.apellido.lower()

List.CRITERION_FUNCTIONS["apellido"] = criterio_apellido



#b
def alumnos_que_no_desaprobaron_ningun_parcial(alumnos):
    lista = List()
    for a in alumnos:
        desaprobo = False
    for parcial in a.parciales:
        if parcial.nota < 6:
                desaprobo = True
        if not desaprobo:
            lista.append(a)

        if lista:
          print("Alumnos que no desaprobaron ningn parcial:")
          lista.show()
        else:
          print("Todos los alumnos desaprobaron")


#c
def alumnos_con_promedio_mayor_a_889(alumnos):
    lista = List()
    for a in alumnos:
        total = 0
        cantidad = 0
        for parcial in a.parciales:
            total += parcial.nota
            cantidad += 1
        if cantidad > 0:
            promedio = total / cantidad
            if promedio > 8.89:
                lista.append(a)

    if lista:
        print("Alumnos con promedio mayor a 8,89:")
        lista.show()
    else:
        print("Ningun alumno tiene promedio mayor a 8,89")
        
        
#d
def alumnos_con_apellido_que_empieza_con_l(alumnos):
    lista = List()
    for a in alumnos:
        if a.apellido[0].lower() == 'L':  
            lista.append(a)

    if lista:
        print("Alumnos cuyo apellido empieza con L:")
        lista.show()
    else:
        print("No hay alumnos cuyo apellido empiece con L")

#e
def mostrar_promedio_de_alumnos(alumnos):
    for a in alumnos:
        total = 0
        cantidad = 0
        for parcial in a.parciales:
            total += parcial.nota
            cantidad += 1
        if cantidad > 0:
            promedio = total / cantidad
            print(f"{a.nombre} {a.apellido}: promedio {promedio:.2f}")
        else:
            print(f"{a.nombre} {a.apellido}: no tiene parciales")





mostrar_alumnos_ordenados_por_apellido(alumnos)
alumnos_que_no_desaprobaron_ningun_parcial(alumnos)
alumnos_con_promedio_mayor_a_889(alumnos)
alumnos_con_apellido_que_empieza_con_l(alumnos)
mostrar_promedio_de_alumnos(alumnos)
