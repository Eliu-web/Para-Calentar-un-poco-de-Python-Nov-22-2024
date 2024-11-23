print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea

def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

# Ejemplo de uso
print(superposicion([1, 2, 3], [4, 5, 6]))  # Salida: False
print(superposicion([1, 2, 3], [3, 4, 5]))  # Salida: True
print(superposicion(['a', 'b', 'c'], ['x', 'y', 'z', 'a']))  # Salida: True