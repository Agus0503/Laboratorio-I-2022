'''Es la gala final de Gran Hermano y la producción nos pide un programa para contar
los votos de los televidentes y saber cuál será el participante que ganará el juego.
Los participantes finalistas son: Nacho, Julieta y Marcos.
El televidente debe ingresar:
● Nombre del votante
● Edad del votante (debe ser mayor a 13)
● Género del votante (masculino, femenino, otro)
● El nombre del participante a quien le dará el voto positivo.
No se sabe cuántos votos entrarán durante la gala.

Se debe informar al usuario:
A. El promedio de edad de las votantes de género femenino
B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
Nacho o Julieta.
C. Nombre del votante más joven que votó a Nacho.
D. Nombre de cada participante y porcentaje de los votos qué recibió.
E. El nombre del participante que ganó el reality (El que tiene más votos)'''

#Almacenamiento de votos por televidente
cantidad_votantes = 0
cantidad_votantes_femenino = 0
cantidad_votantes_masculino = 0

#Almacenamiento de votos por participante
cantidad_votos_nacho = 0
cantidad_votos_marcos = 0
cantidad_votos_julieta = 0

edad_total_femenino = 0
edad_votante_mas_joven_nacho = 0

while True:
    print("\nBienvenido televidente porfavor ingrese sus datos aqui abajo")
    nombre = str(input("Ingrese nombre: "))

    edad = int(input("Ingrese edad: "))
    while edad < 13:
        edad = int(input("ERROR, ingrese una edad mayor a 13 años: "))
        
    genero = str(input("Ingrese genero, m = masculino, f = femenino, x = otro : "))
    while genero != 'm' and  genero != 'f' and genero != 'x':
        genero = str(input("Ingrese genero, m = masculino, f = femenino, x = otro : "))
        
    nombre_participante = str(input("Nombre del participante al que votara (Nacho, Julieta o Marcos): "))
    while nombre_participante != 'Nacho' and  nombre_participante != 'Julieta' and nombre_participante != 'Marcos':
        nombre_participante = str(input("Nombre del participante al que votara (Nacho, Julieta o Marcos): "))
    
    if genero == 'f':
        cantidad_votantes_femenino += 1
        edad_total_femenino += edad
        
    if genero == 'm' and edad >= 25 and edad <= 40:
        if nombre_participante == "Nacho" or nombre_participante == "Julieta":
            cantidad_votantes_masculino += 1

    match nombre_participante:
        case "Julieta":
            cantidad_votos_julieta += 1
        case "Marcos":
            cantidad_votos_marcos += 1
        case "Nacho":
            cantidad_votos_nacho += 1
            if edad < edad_votante_mas_joven_nacho or cantidad_votantes == 0:
                edad_votante_mas_joven_nacho = edad
                nombre_votante_joven_nacho = nombre
        
    cantidad_votantes += 1
    
    confirmacion = input("Desea cargar otro voto? (si/no): ")
    if confirmacion != "si":
        break
    

if cantidad_votantes_femenino == 0:
    promedio_voto_femenino = 0
    print("No hubo votantes femeninos")
else:
    promedio_voto_femenino = edad_total_femenino / cantidad_votantes_femenino 
    print(f"El promedio de edad de votos de genero femenino es: {promedio_voto_femenino}")

print(f"La cantidad de personas de género masculino entre 25 y 40 años que votaron a Nacho o Julieta son: {cantidad_votantes_masculino}")

if cantidad_votos_nacho == 0:
    print("Nacho no obtuvo votos")
else:
    print(f"El votante mas joven que voto a nacho fue: {nombre_votante_joven_nacho}")

total_votos = cantidad_votos_nacho + cantidad_votos_julieta + cantidad_votos_marcos
porcentaje_votos_nacho = (cantidad_votos_nacho / cantidad_votantes) * 100
porcentaje_votos_marcos = (cantidad_votos_marcos / cantidad_votantes) * 100
porcentaje_votos_julieta = (cantidad_votos_julieta / cantidad_votantes) * 100

if cantidad_votos_julieta > cantidad_votos_marcos and cantidad_votos_julieta > cantidad_votos_nacho:
    print("Julieta gano")
elif cantidad_votos_nacho > cantidad_votos_julieta and cantidad_votos_nacho > cantidad_votos_marcos:
    print("Nacho gano")
elif cantidad_votos_marcos > cantidad_votos_julieta and cantidad_votos_marcos > cantidad_votos_nacho:
    print("Marcos gano")
else:
    print("Hay empate")