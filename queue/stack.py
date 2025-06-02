from typing import Any, Optional


class Stack:

    def __init__(self):  # Constructor de la clase
        self.__elements = [] # lista privada que guarda los elementos de la pila


    def push(self, value: Any) -> None:  # Apila un elemento
        self.__elements.append(value) # Agrega el valor al final de la lista (arriba de la fila)

    def pop(self) -> Optional[Any]:  # Desapila un elemento (saca el ultimo)

        return (
            self.__elements.pop()  # Si hay elementos, saca el ultimo y lo devuelve
            if self.__elements
            else None  # Si la pila esta vacia, devuelve None
        )

    def size(self) -> int:  # Devuelve la cantidad de elementos en la pila
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:  # Muestra el elemento en el tope sin quitarlo
        return (
            self.__elements[-1]
            if self.__elements
            else None   # Si esta vacia, devuelve None
        )

    def show(self):    # Muestra los elementos de la pila sin modificarlos permanentemente
        aux_stack = Stack()  # Crea una pila auxiliar para conservar el orden
        while self.size() > 0:   # Mientras la pila original tenga elementos
            value = self.pop()  # Saca un elemento
            print(value)    # Lo muestra por pantalla
            aux_stack.push(value)  # Lo guarda en la pila auxiliar
        
        while aux_stack.size() > 0:  # Luego, vuelve a colocar todo en la pila original
            self.push(aux_stack.pop())
