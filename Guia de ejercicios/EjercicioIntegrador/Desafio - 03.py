'''Desafio #03
Diego Agustin Ostua Larramendia, 1D
'''

from os import system
import re
from data_stark import lista_personajes


def extraer_iniciales(nombre_heroe:str):
    """_summary_
        Extraigo iniciales del nombre del heroe que recibo por parametro
    Args:
        nombre_heroe (str): nombre del heroe proveniente de la lista de personajes
    Returns:
        str: String con las iniciales extraidas del nombre recibido
    """    
    if not nombre_heroe.strip():
        return 'N/A'
    
    nombre_heroe = nombre_heroe.replace('-', ' ')
    
    palabras = nombre_heroe.split()
    palabras_filtradas = []
    for palabra in palabras:
        if palabra.lower() != 'the':
            palabras_filtradas.append(palabra)
    
    iniciales = ''
    for palabra in palabras_filtradas:
        iniciales += palabra[0] + '.'
    
    return iniciales


def definir_iniciales_nombre(heroe:dict):
    """_summary_
        Recibe un diccionario(heroe) por parametro
    Args:
        heroe (dict): heroe proveniente de la lista de personajes
    Returns:
        bool : True si pudo crear la clave
               False si el tipo de dato recibido es incorrecto o la clave no existe
    """    
    if type(heroe) != dict or 'nombre' not in heroe:
        return False
    
    heroe['iniciales'] = extraer_iniciales(heroe['nombre'])
    return True


def agregar_iniciales_nombre(lista:list):
    """_summary_
        Itero sobre la lista pasándole cada héroe a la función definir_iniciales_nombre y agregar a cada uno
        la clave 'iniciales' y su respectivo valor
    Args:
        lista (list): lista de personajes
    Returns:
        bool: False si el dato recibido no es una lista o si esta vacia
              True si se ejecuto correctamente
    """    
    if type(lista) != list or len(lista) < 1:
        print("El origen de datos no contiene el formato correcto")
        return False
    
    for personaje in lista:
        definir_iniciales_nombre(personaje)
    
    return True
    
'''Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
como parámetro:
● lista_heroes: la lista de personajes
La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
las iniciales a los diccionarios contenidos en la lista_heroes
Luego deberá imprimir la lista completa de los nombres de los personajes
seguido de las iniciales encerradas entre paréntesis ()
Se deberá validar:
● Que lista_heroes sea del tipo lista
● Que la lista contenga al menos un elemento
Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
viñeta) seguido de un espacio.
Ejemplo de salida:
* Howard the Duck (H.D.)
* Rocket Raccoon (R.R.)
...
La función no retorna nada'''

def stark_imprimir_nombres_con_iniciales(lista:list):
    
    if type(lista) != list:
        return 