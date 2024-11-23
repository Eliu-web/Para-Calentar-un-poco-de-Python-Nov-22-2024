print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea
def es_palindromo(palabra):
    # Convertimos la palabra a minúsculas para una comparación sin distinción de mayúsculas
    palabra = palabra.lower()
    # Invertimos la palabra
    palabra_invertida = palabra[::-1]
    # Comparamos la palabra original con la palabra invertida
    return palabra == palabra_invertida

# Ejemplo de uso
print(es_palindromo("radar"))  # Salida: True
print(es_palindromo("hola"))   # Salida: False
print(es_palindromo("Anita lava la tina"))  # Salida: True (considerando espacios y mayúsculas)