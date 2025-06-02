from typing import Any, Optional  # 

class Queue:  # Definicion de la clase Cola (primero en entrar, primero en salir)

    def __init__(self):
        self.__elements = []  # Lista privada que guarda los elementos de la cola

    def arrive(self, value: Any) -> None:
        self.__elements.append(value)  # Agrega un valor al final de la cola

    def attention(self) -> Optional[Any]:
        # Si hay elementos, saca y devuelve el primero; si no, devuelve None
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def size(self) -> int:
        return len(self.__elements)  # Devuelve la cantidad de elementos en la cola
    
    def on_front(self) -> Optional[Any]:
        # Devuelve el primer elemento sin sacarlo, o None si esta vacia
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def move_to_end(self) -> Optional[Any]:
        # Mueve el primer elemento al final (si la cola no esta vacia)
        if self.__elements:
            value = self.attention()  # Saca el primero
            self.arrive(value)        # Lo vuelve a poner al final
            return value              # Devuelve el valor movido
    
    def show(self):
        # Muestra todos los elementos en orden
        for i in range(len(self.__elements)):
            print(self.move_to_end())  # Imprime y rota cada elemento una vez
