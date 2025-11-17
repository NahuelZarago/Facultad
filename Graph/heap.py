from typing import Any

# ============================================================
# ========================== HEAP MAX =========================
# ============================================================

class HeapMax:

    def __init__(self):
        # Lista donde se almacenan los elementos del heap
        self.elements = []
    
    def size(self) -> int:
        # Devuelve cuántos elementos hay en el heap
        return len(self.elements)

    def add(self, value: Any) -> None:
        # Agrega el valor al final y lo hace flotar
        self.elements.append(value)
        self.float(self.size() - 1)
    
    def remove(self) -> Any:
        # Intercambia la raíz con el último, elimina el mayor y hunde la nueva raíz
        last = self.size() - 1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        # Hace subir un elemento mientras sea mayor que su padre
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        # Hace bajar un elemento mientras alguno de sus hijos sea mayor
        left_son = (2 * index) + 1
        control = True

        while control and left_son < self.size():
            right_son = left_son + 1
            mayor = left_son

            # Selecciona el hijo mayor
            if right_son < self.size() and self.elements[right_son] > self.elements[mayor]:
                mayor = right_son

            # Si el hijo mayor es mayor que el padre, intercambiar
            if self.elements[index] < self.elements[mayor]:
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False

    def interchange(self, index_1: int, index_2: int) -> None:
        # Intercambia dos posiciones del heap
        self.elements[index_1], self.elements[index_2] = \
        self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        # Extrae todos los elementos en orden del mayor al menor
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # Inserta con prioridad: (prioridad, valor)
        self.add([priority, value])
    
    def attention(self) -> Any:
        # Devuelve el elemento de mayor prioridad
        return self.remove()


# ============================================================
# ========================== HEAP MIN =========================
# ============================================================

class HeapMin:

    def __init__(self):
        # Lista donde se guarda el montículo mínimo
        self.elements = []
    
    def size(self) -> int:
        # Devuelve cuántos elementos hay en el heap
        return len(self.elements)

    def add(self, value: Any) -> None:
        # Agrega un elemento y lo hace flotar hacia arriba
        self.elements.append(value)
        self.float(self.size() - 1)
    
    def search(self, value):
        # Busca la posición de un elemento según su valor
        # usado por dijkstra para encontrar nodos
        for index, element in enumerate(self.elements):
            # element = [priority, [value, vertex, previous]]
            if element[1][0] == value:
                return index

    def remove(self) -> Any:
        # Elimina y devuelve el mínimo (la raíz)
        last = self.size() - 1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        # Hace flotar un elemento si su prioridad es menor que la del padre
        father = (index - 1) // 2

        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        # Hace descender el elemento si alguno de los hijos es menor
        left_son = (2 * index) + 1
        control = True

        while control and left_son < self.size():

            right_son = left_son + 1
            minor = left_son

            # Elige el hijo menor
            if right_son < self.size() and self.elements[right_son] < self.elements[minor]:
                minor = right_son

            # Si el hijo es menor que el padre, bajar
            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False

    def interchange(self, index_1: int, index_2: int) -> None:
        # Intercambia dos elementos en el heap
        self.elements[index_1], self.elements[index_2] = \
        self.elements[index_2], self.elements[index_1]

    def heapsort(self) -> list:
        # Extrae elementos ordenados de menor a mayor
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # Inserta un valor con prioridad
        self.add([priority, value])
    
    def attention(self) -> Any:
        # Devuelve el elemento de menor prioridad
        return self.remove()

    def change_priority(self, index, new_priority):
        # Cambia la prioridad de un elemento y ajusta su posición
        if index < len(self.elements):

            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority

            # Si la prioridad aumenta → hundir
            if new_priority > previous_priority:
                self.sink(index)

            # Si la prioridad baja → flotar
            elif new_priority < previous_priority:
                self.float(index)
