'''Se nos pide realizar un programa que le pida al usuario una N cantidad de veces y
calcular la máxima diferencia en la secuencia de números ingresada.'''

def calcular_maxima_diferencia(numeros):
    maxima_diferencia = 0
    maximo = numeros[0]
    minimo = numeros[0]
    
    for numero in numeros:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero
    maxima_diferencia = maximo - minimo
    return maxima_diferencia

n = int(input("Cantidad de números a ingresar: "))

numeros = []
for i in range(n):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

maxima_diferencia = calcular_maxima_diferencia(numeros)

print("La máxima diferencia entre los números ingresados es:", maxima_diferencia)
