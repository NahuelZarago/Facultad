from typing import Any, Optional  # Importa tipos opcionales para anotaciones de tipo

class List(list):  # Define una clase personalizada que hereda de list (lista nativa de Python)

    CRITERION_FUNCTIONS = {}  # Diccionario de clase para guardar funciones de criterio de orden o búsqueda

    def add_criterion(self, key_criterion: str, function):  
        # Agrega una función de criterio al diccionario usando una clave
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None:
        # Muestra todos los elementos de la lista
        for element in self:
            print(element)

    def delete_value(self, value, key_value: str = None) -> Optional[Any]:
        # Elimina un valor de la lista según un criterio (si se da), usando búsqueda binaria
        index = self.search(value, key_value)  # Busca el índice del valor
        return self.pop(index) if index is not None else index  # Lo elimina y devuelve, o None si no se encontró

    # Este método está comentado, pero se intuye que sería para insertar valores en la lista
    # def insert_value(self, value: Any) -> None:
    #     pass

    def sort_by_criterion(self, criterion_key: str = None) -> None:
        # Ordena la lista usando un criterio (si se especifica)
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)  # Busca la función criterio

        if criterion is not None:
            self.sort(key=criterion)  # Ordena usando la función como clave
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()  # Ordena directamente si son tipos simples
        else:
            print('criterio de orden no encontrado')  # No se pudo ordenar

    def search(self, search_value, search_key: str = None) -> int:
        # Búsqueda binaria del valor usando el criterio dado (si hay)
        self.sort_by_criterion(search_key)  # Asegura que la lista esté ordenada por el criterio

        start = 0
        end = len(self) - 1
        middle = (start + end) // 2  # Inicializa el punto medio

        while start <= end:
            # Obtiene la función de criterio (si se dio)
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            
            # Si no hay criterio y los elementos no son básicos (int, str, bool), no se puede buscar
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]  # Aplica el criterio si existe
            if value == search_value:
                return middle  # Valor encontrado
            elif value < search_value:
                start = middle + 1  # Buscar en la mitad derecha
            else:
                end = middle - 1  # Buscar en la mitad izquierda
            middle = (start + end) // 2  # Actualiza el medio

        return None  # Si no lo encontró
