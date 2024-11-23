print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea
def es_vocal(caracter):
    # Definimos un conjunto de vocales
    vocales = 'aeiouAEIOU'
    # Verificamos si el carácter está en el conjunto de vocales
    return caracter in vocales

# Ejemplo de uso
print(es_vocal('a'))  # Salida: True
print(es_vocal('B'))  # Salida: False
print(es_vocal('e'))  # Salida: True
print(es_vocal('z'))  # Salida: False