'''Desafío #01:

Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos, utilizando un menú que permita acceder a cada uno de los puntos por separado.
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con (No Tiene).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
'''
# Importacion de librerias
from data_stark import lista_personajes
from os import system

def imprimir_superheroes_por_genero(lista,genero):
    
    system('cls')
    for personaje in lista:
        genero = genero.upper()
        if personaje['genero'] == genero:
            print(personaje['nombre'])

def obtener_superheroe_mas_alto(genero):
    personaje_mas_alto = None  # Utilizo tambien como bandera
    personajes_mas_altos = []

    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            altura = float(personaje["altura"]) # convierto la altura a valor numerico para comparar
            if personaje_mas_alto is None or altura > float(personaje_mas_alto["altura"]):
                personaje_mas_alto = personaje  # Guardo el personaje_mas_alto
                personajes_mas_altos = [personaje]
            elif altura == float(personaje_mas_alto['altura']):
                # En caso de encontrar otro personaje con el maximo de altura lo agrego a la lista
                personajes_mas_altos.append(personaje)

    for i in range(len(personajes_mas_altos)):
        personaje = personajes_mas_altos[i]
        for dato in personaje:
            print(dato + ":", personaje[dato])

    return personajes_mas_altos

def obtener_superheroe_mas_bajo(genero):
    personaje_mas_bajo = None
    personajes_mas_bajos = []

    for personaje in lista_personajes:
        if personaje['genero'] == genero:
            altura = float(personaje["altura"])
            if personaje_mas_bajo is None or altura < float(personaje_mas_bajo['altura']):
                personaje_mas_bajo = personaje
                personajes_mas_bajos = [personaje]
            elif altura == float(personaje_mas_bajo['altura']):
                personajes_mas_bajos.append(personaje)

    for i in range(len(personajes_mas_bajos)):
        personaje = personajes_mas_bajos[i]
        for dato in personaje:
            print(dato + ":", personaje[dato])

    return personajes_mas_bajos

def obtener_altura_por_genero(altura,genero):
    
    superheroe = None
    altura = altura.lower()
    
    system('cls')
    if altura == "alto":
        genero = genero.upper()
        if genero == 'M' or genero == 'F':
            print(f"\nEl/los personaje(s) más alto(s) de genero '{genero}' es/son:")
            superheroe = obtener_superheroe_mas_alto(genero)
    elif altura == "bajo":
        genero = genero.upper()
        if genero == 'M' or genero == 'F':
            print(f"\nEl/los personaje(s) más bajo(s) de genero '{genero}' es/son:")
            superheroe = obtener_superheroe_mas_bajo(genero)
    else:
        print("La altura ingresada no es válida")

    return superheroe

def calcular_promedio_altura_genero(lista, genero):
    acumulador = 0
    contador = 0
    genero = genero.upper()
    
    for personaje in lista:
        if personaje['genero'] == genero:
            acumulador += float(personaje['altura'])
            contador += 1

    system('cls')
    if contador > 0:
        promedio_altura = acumulador / contador
        print(f"El promedio de altura de los personajes de género {genero} es: {round(promedio_altura,2)}")
    else:
        print(f"No se encontraron personajes de género {genero} en la lista.")


def imprimir_mayor_menor_altura_generos():
    '''
        Calculo y muestro la altura mayor y menor de ambos generos (M y F)
    '''
    
    personajes_mas_altos_genero_m = obtener_altura_por_genero('alto','m')
    personajes_mas_altos_genero_f = obtener_altura_por_genero('alto','F')
    personajes_mas_bajos_genero_m = obtener_altura_por_genero('bajo','m')
    personajes_mas_bajos_genero_f = obtener_altura_por_genero('bajo','f')

    system('cls')
    print(f"El/los personaje/s mas alto/s de genero 'M' es/son:")
    imprimir_dato_unico(personajes_mas_altos_genero_m, 'nombre')

    print(f"El/los personaje/s mas bajo/s de genero 'M' es/son:")
    imprimir_dato_unico(personajes_mas_bajos_genero_m, 'nombre')
    
    print(f"El/los personaje/s mas alto/s de genero 'F' es/son:")
    imprimir_dato_unico(personajes_mas_altos_genero_f, 'nombre')

    print(f"El/los personaje/s mas bajo/s de genero 'F' es/son:")
    imprimir_dato_unico(personajes_mas_bajos_genero_f, 'nombre')
    

def filtrar_por_tipo(lista,tipo):
    # Diccionario para almacenar la cantidad de superhéroes por tipo de dato (color de ojos,pelo,etc)
    contador_tipo = {}

    for personaje in lista:
        
        if tipo not in personaje: 
            personaje[tipo] = 'Unknown'  # si el color de ojos(ej) no está definido, asigno "Unknown"

        color_dato = personaje[tipo]
        
        if color_dato in contador_tipo:
            contador_tipo[color_dato] += 1
        else:
            contador_tipo[color_dato] = 1
    
    for dato in contador_tipo:
        cantidad = contador_tipo[dato]
        if dato == '' or dato == 'Unknown':
            dato = 'No tiene'
        print(dato + ":", cantidad)
     

def listar_personajes_por_tipo(lista, tipo):
    """
        Imprime los personajes agrupados por el tipo especificado
        ----------
        Parametros
        ----------
        lista -> una lista de diccionarios(lista de personajes en este caso)
        tipo -> Para indicar sobre que tipo trabajar(en este caso, color de pelo, color de ojos,etc)
        
    """
    personajes_por_tipo = {}

    if tipo not in lista[0].keys():
        print("El tipo especificado no es válido.")
        return

    for personaje in lista:
        valor_tipo = personaje[tipo]

        if valor_tipo not in personajes_por_tipo:
            personajes_por_tipo[valor_tipo] = []
        personajes_por_tipo[valor_tipo].append(personaje)

    system('cls')
    print(f"\nPersonajes por {tipo}: ")
    for valor, personajes in personajes_por_tipo.items():
        print(tipo.capitalize() + ":", valor)
        for personaje in personajes:
            print(f"- Nombre: {personaje['nombre']}")


def imprimir_dato_unico(lista, key):
    '''
    Esta función se creo especialmente con el propisito de imprimir el valor de un personaje(por ej) de una lista de diccionarios.
    ----------
    Parametros
    ----------
    lista -> una lista de diccionarios
    key -> clave que representa el valor especifico con el que se desea trabajar
    '''
    for i in range(len(lista)):
        personaje = lista[i]
        if key in personaje:
            for clave in personaje:
                if clave == key:
                    print(personaje[clave])
        else:
            print("ERROR")
            system("pause")

# FUNCION PARA MUESTREO DE MENU DE OPCIONES
def imprimir_menu_desafio01():
    menu = ["1.Imprimir por consola el nombre de cada superhéroe de género M",
            "2.Imprimir por consola el nombre de cada superhéroe de género F",
            "3.Determinar cuál es el superhéroe más alto de género M",
            "4.Determinar cuál es el superhéroe más alto de género F",
            "5.Determinar cuál es el superhéroe más bajo de género M",
            "6.Determinar cuál es el superhéroe más bajo de género F",
            "7.Determinar la altura promedio de los superhéroes de género M",
            "8.Determinar la altura promedio de los superhéroes de género F",
            "9.Informar el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems 3 a 6)",
            "10.Determinar cuántos superhéroes tienen cada tipo de color de ojos",
            "11.Determinar cuántos superhéroes tienen cada tipo de color de pelo",
            "12.Determinar cuántos superhéroes tienen cada tipo de inteligencia",
            "13.Listar todos los superhéroes agrupados por color de ojos",
            "14.Listar todos los superhéroes agrupados por color de pelo",
            "15.Listar todos los superhéroes agrupados por tipo de inteligencia",
            "16.SALIR"]
    for opcion in menu:
        print(opcion)

# ------------------ BUCLE PRINCIPAL ------------------

while True:

    system('cls')
    imprimir_menu_desafio01()
    opcion = int(input("Ingrese una opcion: "))
    while opcion < 1 or opcion > 16:
        system('cls')
        imprimir_menu_desafio01()
        opcion = int(input("Error,ingrese una opcion valida: "))
    
    match opcion:
        
        case 1:
            imprimir_superheroes_por_genero(lista_personajes,'m')
        case 2:
            imprimir_superheroes_por_genero(lista_personajes,'f')
        case 3:
            obtener_altura_por_genero('alto','m')
        case 4:
            obtener_altura_por_genero('ALTO','F')
        case 5:
            obtener_altura_por_genero('bajo','M')
        case 6:
            obtener_altura_por_genero('BAJO','f')
        case 7:
            calcular_promedio_altura_genero(lista_personajes,'m')
        case 8:
            calcular_promedio_altura_genero(lista_personajes,'F')
        case 9:
            imprimir_mayor_menor_altura_generos()
        case 10:
            print("La cantidad de superheroes por color de ojos son:")
            filtrar_por_tipo(lista_personajes,'color_ojos')
        case 11:
            print("La cantidad de superheroes por color de pelo son:")
            filtrar_por_tipo(lista_personajes,'color_pelo')
        case 12:
            print("La cantidad de superheroes por tipo de inteligencia son:")
            filtrar_por_tipo(lista_personajes,'inteligencia')
        case 13:
            listar_personajes_por_tipo(lista_personajes,'color_ojos')
        case 14:
            listar_personajes_por_tipo(lista_personajes,'color_pelo')
        case 15:
            listar_personajes_por_tipo(lista_personajes,'inteligencia')
        case 16:
            print("Programa Finalizado")
            break

    input("Presiona Enter para continuar...")
