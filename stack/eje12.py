#Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
#que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

#No se nada de Star Wars
pila = ["Leia Organa", "Monito1", "Monito2", "Monito3"]

def funcion(pila):
    if "Leia Organa" in pila:
        print("Se encuentra Leia Organa")
        return True
    elif "Boba Fett" in pila:
        print("Se encuentra Boba Fett")
        return True
    else: 
        print("No se encuentran ninguno de los 2")
        return False
print(pila)

funcion(pila)
