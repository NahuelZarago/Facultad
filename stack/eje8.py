#Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
#cartas de baraja española–,resolver las siguientes actividades:
#a. generar las cartas del mazo de forma aleatoria;
#b. separar la pila mazo en cuatro pilas una por cada palo;
#c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.
import random


palos = ["espada", "basto", "copa", "oro"]
numeros = list(range(1, 13))  # 1 al 12

mazo = [(numero, palo) for palo in palos for numero in numeros]
random.shuffle(mazo)

print("Mazo mezclado:")
print(mazo)

pilas_por_palo = {
    "espada": [],
    "basto": [],
    "copa": [],
    "oro": []
}

while mazo:
    carta = mazo.pop()
    pilas_por_palo[carta[1]].append(carta)

print("\nCartas por palo:")
for palo, pila in pilas_por_palo.items():
    print(f"{palo.capitalize()}: {pila}")

palo_a_ordenar = "espada"
pilas_por_palo[palo_a_ordenar] = sorted(pilas_por_palo[palo_a_ordenar], key=lambda carta: carta[0])

print(f"Pila de {palo_a_ordenar} ordenada de forma creciente:")
print(pilas_por_palo[palo_a_ordenar])
