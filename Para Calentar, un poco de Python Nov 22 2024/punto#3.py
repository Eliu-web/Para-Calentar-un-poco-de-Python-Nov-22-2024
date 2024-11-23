print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea
def longitud(objeto):
    contador = 0
    for _ in objeto:
        contador += 1
    return contador

# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
cadena = "Hola, mundo!"

print("Longitud de la lista:", longitud(lista))  # Salida: 5
print("Longitud de la cadena:", longitud(cadena))  # Salida: 13