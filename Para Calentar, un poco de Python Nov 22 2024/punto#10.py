print ()#Salto de linea
print ("Jesus Eliu Velaquez Mares")
print ()#Salto de linea
def histograma(lista):
    for numero in lista:
        # Imprimir el número seguido de asteriscos
        print(f"{numero}: {'*' * numero}")

# Ejemplo de uso
numeros = [3, 5, 2, 8, 6]
histograma(numeros)