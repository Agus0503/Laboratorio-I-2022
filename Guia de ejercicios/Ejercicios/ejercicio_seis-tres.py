'''Realizar una carga indefinida de números, añadirlos a una lista e indicar que posición
de memoria es la que mas ocurrencias tiene dentro de esa lista.'''

numeros = []

while True:
    
    numero = float(input("Ingrese un numero: "))
    numeros.append(int(numero))
    
    mas_ocurrencias = 0
    for i in range(len(numeros)):
        ocurrencias = 0
        for j in range(len(numeros)):
            if numeros[j] == numeros[i]:
                ocurrencias += 1
            if ocurrencias > mas_ocurrencias:
                mas_ocurrencias = ocurrencias
                posicion_mas_ocurrencias = i
    
    confirmacion = input("Desea ingresar otro numero? (s/n): ")
    while confirmacion != 's' and confirmacion != 'n':
        confirmacion = input("Porfavor ingrese una opcion valida,desea ingresar otro numero? (s/n): ")
    # Si el usuario ingresa "s", se rompe el ciclo y se muestra el diccionario completo
    if confirmacion == "n":
        break

print(f"La posicion con mas ocurrencias es: {posicion_mas_ocurrencias} con {mas_ocurrencias} ocurrencias detectadas")