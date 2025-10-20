# 16. Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
# criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
# siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con
# un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.


from heap import HeapMax  

#cola prioridad
cola_impresion = HeapMax()

#a
cola_impresion.arrive("A", 1)
cola_impresion.arrive("B", 1)
cola_impresion.arrive("C", 1)

print("Cola inicial:")
print(cola_impresion.elements)
print()

#b
primero = cola_impresion.attention()
print(f"Imprimiendo: {primero[1]}\n")

#c
cola_impresion.arrive("Documento D - TI", 2)
cola_impresion.arrive("Documento E - TI", 2)

#d
cola_impresion.arrive("Documento F - Gerente", 3)

print("Cola despues de cargar TI y Gerente:")
print(cola_impresion.elements)
print()

#e
for _ in range(2):
    doc = cola_impresion.attention()
    print(f"Imprimiendo: {doc[1]}")

print()

#f
cola_impresion.arrive("Documento G - Empleado", 1)
cola_impresion.arrive("Documento H - Empleado", 1)
cola_impresion.arrive("Documento I - Gerente", 3)

print("Cola despues de nuevas cargas:")
print(cola_impresion.elements)
print()

#g
print("Imprimiendo todos los documentos restantes:")
while cola_impresion.size() > 0:
    doc = cola_impresion.attention()
    print(f"Imprimiendo: {doc[1]}")
