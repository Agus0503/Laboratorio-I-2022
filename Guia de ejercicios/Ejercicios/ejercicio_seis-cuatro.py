'''Debemos desarrollar un algoritmo que permita computar los votos del Senado de
Berlinberlín. Se deberá ingresar el nombre de cada senador y si está Presente o no en
la sesión. Si el senador está presente, se deberá pedir el valor del voto
El voto de los senadores berliberlineses puede ser Afirmativo, Negativo o Abstención
(validar). El valor por defecto para los senadores ausentes será Abstención.
Se deberá Informar:

o Cantidad total de senadores.
o Cantidad de senadores presentes.
o Cantidad y porcentaje de votos afirmativos.
o Cantidad y porcentaje de votos negativos.
o Cantidad y porcentaje de abstenciones.
o Generar una lista de senadores por cada tipo de voto y mostrarlas por
pantalla.'''

senadores = []
senadores_presentes = []
senadores_voto_afirmativo = []
senadores_voto_negativo = []
senadores_abstenciones = []

while True:
    
    nombre = input("\nIngrese nombre: ")
    
    esta_presente = str(input(f"El senador {nombre} esta presente? (s/n): "))
    esta_presente = esta_presente.lower()
    while esta_presente != 's' and esta_presente != 'n':
       esta_presente = input(f"Porfavor ingrese una opcion valida,El senador {nombre} esta presente? (s/n): ")
       esta_presente.lower()

    if esta_presente == 's':
        senadores_presentes.append(nombre)
        voto = input("Cual es su voto?\n A = Afirmativo, N = Negativo, Ab = Abstencion : ")
        voto = voto.lower()
        while voto != 'a' and voto != 'n' and voto != 'ab':
            voto = input(f"Porfavor ingrese una opcion valida,\n A = Afirmativo, N = Negativo, Ab = Abstencion :  ")
            voto = voto.lower()
            
        if voto == 'a':
            senadores_voto_afirmativo.append(nombre)
        elif voto == 'n':
            senadores_voto_negativo.append(nombre)
        elif voto == 'ab':
            senadores_abstenciones.append(nombre)
    else:
        voto = 'ab'                    
        senadores_abstenciones.append(nombre)

    senadores.append(nombre)
    
    confirmacion = input("Desea ingresar otro nombre? (s/n): ")
    confirmacion = confirmacion.lower()
    while confirmacion != 's' and confirmacion != 'n':
        confirmacion = input("Porfavor ingrese una opcion valida,desea ingresar otro nombre? (s/n): ")
        confirmacion = confirmacion.lower()
    if confirmacion == "n":
        break

cantidad_total_senadores = len(senadores) #Tambien equivale a la cantidad total de votos
cantidad_senadores_presentes = len(senadores_presentes)
cantidad_votos_afirmativos = len(senadores_voto_afirmativo)
cantidad_votos_negativos = len(senadores_voto_negativo)
cantidad_abstenciones = len(senadores_abstenciones)

print(f"\nCantidad senadores: {cantidad_total_senadores}")
print(f"Cantidad de senadores presentes: {cantidad_senadores_presentes}")

print(f"\nCantidad afirmativos: {cantidad_votos_afirmativos}")
if cantidad_votos_afirmativos > 0:
    porcentaje_votos_afirmativos = (cantidad_votos_afirmativos / cantidad_total_senadores) * 100
    print(f"Porcentaje de votos afirmativos: {round(porcentaje_votos_afirmativos,2)}")

print(f"\nCantidad negativos: {cantidad_votos_negativos}")
if cantidad_votos_negativos > 0:
    porcentaje_votos_negativos = (cantidad_votos_negativos / cantidad_total_senadores) * 100
    print(f"Porcentaje de votos negativos: {round(porcentaje_votos_negativos,2)}")

print(f"\nCantidad abstenciones: {cantidad_abstenciones}")
if cantidad_abstenciones > 0:
    porcentaje_abstenciones = (cantidad_abstenciones / cantidad_total_senadores) * 100
    print(f"Porcentaje de abstenciones: {round(porcentaje_abstenciones,2)}\n")

print(f"Lista de senadores que votaron afirmativamente: {senadores_voto_afirmativo}")
print(f"Lista de senadores que votaron negativamente: {senadores_voto_negativo}")
print(f"Lista de senadores que se abstuvieron: {senadores_abstenciones}")
