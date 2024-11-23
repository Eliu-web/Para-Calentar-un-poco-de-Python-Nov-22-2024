print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea
def sum(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multip(lista):
    total = 1
    for numero in lista:
        total *= numero
    return total

# Ejemplo de uso
numeros = [1, 2, 3, 4]

resultado_suma = sum(numeros)  # Debería devolver 10
resultado_multiplicacion = multip(numeros)  # Debería devolver 24

print("Suma:", resultado_suma)  # Salida: Suma: 10
print("Multiplicación:", resultado_multiplicacion)  # Salida: Multiplicación: 24