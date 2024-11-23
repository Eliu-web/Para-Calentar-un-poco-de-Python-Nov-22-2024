print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea
def inversa(cadena):
    cadena_invertida = ''
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

# Ejemplo de uso
resultado = inversa("estoy probando")
print(resultado)  # Salida: "odnaborp yotse"