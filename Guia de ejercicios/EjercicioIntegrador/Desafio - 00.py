'''Desafío #00:

A. Analizar detenidamente el set de datos
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe 
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo 
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO) 
F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO) 
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO) 
H. Calcular e informar cual es el superhéroe más y menos pesado. 
I. Ordenar el código implementando una función para cada uno de los valores informados. 
J. Construir un menú que permita elegir qué dato obtener
'''
#Importacion de librerias
from data_stark import lista_personajes
from os import system

# ------------------ Declaracion y desarrollo de funciones ------------------

def imprimir_nombres_superheroes():
    for personaje in lista_personajes:
        print(personaje['nombre'])

def imprimir_nombre_altura():
    for personaje in lista_personajes:
        print(f"Nombre: {personaje['nombre']:20s} Altura: {round(float(personaje['altura']), 2):>10}")

def buscar_superheroe_mas_alto():
    personaje_mas_alto = None #Utilizo tambien como bandera 
    personajes_mas_altos = []
    
    for personaje in lista_personajes:
        altura = float(personaje["altura"])   #convierto la altura a valor numerico para comparar
        if personaje_mas_alto is None or altura > float(personaje_mas_alto["altura"]):
            personaje_mas_alto = personaje   #Guardo el personaje_mas_alto
            personajes_mas_altos = [personaje]
        elif altura == float(personaje_mas_alto['altura']):
            personajes_mas_altos.append(personaje) #En caso de encontrar otro personaje con el maximo de altura lo agrego a la lista
    
    print("\nEl/los personaje(s) más alto(s) es/son:")
    for i in range(len(personajes_mas_altos)):
        personaje = personajes_mas_altos[i]
        for dato in personaje:
            print(dato + ":", personaje[dato])


def buscar_superheroe_mas_bajo():
    personaje_mas_bajo = None
    personajes_mas_bajos = []
    
    for personaje in lista_personajes:
        altura = float(personaje["altura"])   # convierto la altura a valor numerico para comparar
        if personaje_mas_bajo is None or altura < float(personaje_mas_bajo['altura']):  
            personaje_mas_bajo = personaje
            personajes_mas_bajos = [personaje]
        elif altura == float(personaje_mas_bajo['altura']):
            personajes_mas_bajos.append(personaje)
        
    print("\nEl/los personaje(s) más bajo(s) es/son:")
    for i in range(len(personajes_mas_bajos)):
        personaje = personajes_mas_bajos[i]
        for dato in personaje:
            print(dato + ":", personaje[dato])

def calcular_promedio_altura():
    acumulador = 0
    
    for personaje in lista_personajes:
        acumulador += float(personaje['altura'])
    
    promedio_altura = acumulador / len(lista_personajes)
    print(f"El promedio de altura de los personajes es: {round(promedio_altura,2)}")
    

def mostrar_mas_alto_y_mas_bajo():
    personaje_mas_alto = None
    personaje_mas_bajo = None
    personajes_mas_altos = []
    personajes_mas_bajos = []
    
    for personaje in lista_personajes:
        altura = float(personaje["altura"])   #convierto la altura a valor numerico para comparar
        if personaje_mas_alto is None or altura > float(personaje_mas_alto["altura"]):
            personaje_mas_alto = personaje
            personajes_mas_altos = [personaje['nombre']] #Corregir aquí: usar lista en lugar de asignación directa
        elif altura == float(personaje_mas_alto['altura']):
            personajes_mas_altos.append(personaje['nombre']) #Corregir aquí: usar append() para agregar a la lista
        
        if personaje_mas_bajo is None or altura < float(personaje_mas_bajo['altura']):  
            personaje_mas_bajo = personaje
            personajes_mas_bajos = [personaje['nombre']] #Corregir aquí: usar lista en lugar de asignación directa
        elif altura == float(personaje_mas_bajo['altura']):
            personajes_mas_bajos.append(personaje['nombre']) #Corregir aquí: usar append() para agregar a la lista
            
    system('cls')
    print("El/los personaje/s mas alto/s es/son: ")
    for i in range(len(personajes_mas_altos)):
        print(personajes_mas_altos[i])
        
    print("El/los personaje/s mas bajo/s es/son: ")
    for i in range(len(personajes_mas_bajos)):
        print(personajes_mas_bajos[i])

def buscar_heroe_mas_y_menos_pesado():
    
    mayor_peso = None
    menor_peso = None
    personajes_mas_pesados = []
    personajes_menos_pesados = []
    
    for personaje in lista_personajes:
        peso = float(personaje["peso"])        
        if menor_peso is None or peso < menor_peso:
            menor_peso = peso
            personajes_menos_pesados = [personaje['nombre']]
        elif peso == menor_peso:
            personajes_menos_pesados.append(personaje['nombre'])
        
        if mayor_peso is None or peso > mayor_peso:
            mayor_peso = peso
            personajes_mas_pesados = [personaje['nombre']]
        elif peso == mayor_peso:
            personajes_mas_pesados.append(personaje['nombre'])
            
    system('cls')
    print(f"El/los personaje/s mas pesado/s es/son: ") 
    for i in range(len(personajes_mas_pesados)):
        print(personajes_mas_pesados[i])
        
    print(f"El/los personaje/s menos pesado/s es/son: ")
    for i in range(len(personajes_menos_pesados)):
        print(personajes_menos_pesados[i])
        

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
def imprimir_menu_desafio00():
    menu = ["1.Imprimir nombre de cada superhéroe",
            "2.Imprimir nombre de cada superhéroe junto a la altura del mismo",
            "3.Determinar cuál es el superhéroe más alto (MÁXIMO)",
            "4.Determinar cuál es el superhéroe más bajo (MÍNIMO)",
            "5.Determinar la altura promedio de los superhéroes",
            "6.Informar nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)",
            "7.Calcular e informar cual es el superhéroe más y menos pesado",
            "8.Salir"]
    for opcion in menu:
        print(opcion)

# ------------------ BUCLE PRINCIPAL ------------------
while True:
    
    system('cls')            
    imprimir_menu_desafio00()
    opcion = int(input("Ingrese una opcion: "))
    while opcion < 1 or opcion > 8:
        system('cls')
        imprimir_menu_desafio00()
        opcion = int(input("Error,ingrese una opcion valida: "))

    match opcion:
        
        case 1:
            imprimir_nombres_superheroes()
        case 2:          
            imprimir_nombre_altura()
        case 3:
            buscar_superheroe_mas_alto()
        case 4:
            buscar_superheroe_mas_bajo()
        case 5:
            calcular_promedio_altura()
        case 6:
            mostrar_mas_alto_y_mas_bajo()
        case 7:
            buscar_heroe_mas_y_menos_pesado()
        case 8:
            print("Programa Finalizado")
            break  
    
    input("Presiona Enter para continuar...")

